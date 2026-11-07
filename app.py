
import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load local environment variables
load_dotenv()

st.set_page_config(
    page_title="AI Mail Assistant",
    page_icon="📧",
    layout="centered"
)


def get_settings():
    """Read credentials from Streamlit Secrets or local .env."""
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        model = st.secrets.get("OPENAI_MODEL", "gpt-6-luna")
    except Exception:
        api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("OPENAI_MODEL", "gpt-6-luna")

    return api_key, model


st.title("📧 AI Mail Assistant")
st.write(
    "Analyze customer emails, identify priorities "
    "and generate professional reply drafts with AI."
)

st.divider()

email_text = st.text_area(
    "Paste the customer email here:",
    height=220,
    placeholder="Hello, I have a question about my order..."
)

analyze_button = st.button(
    "✨ Analyze Email",
    type="primary",
    use_container_width=True
)

if analyze_button:
    if not email_text.strip():
        st.warning("Please enter an email first.")

    else:
        api_key, model = get_settings()

        if not api_key:
            st.error(
                "OpenAI API key not found. "
                "Please configure OPENAI_API_KEY in Streamlit Secrets."
            )
        else:
            try:
                client = OpenAI(api_key=api_key)

                instructions = """
                You are a professional AI email assistant.

                Analyze the customer's email and return:
                1. Category
                2. Priority (Low, Medium, or High)
                3. Sentiment (Positive, Neutral, or Negative)
                4. A short summary
                5. Recommended next steps
                6. A professional reply draft

                Use clear headings and concise language.
                Write the reply draft in the same language
                as the customer's original email.
                Never invent order details or promise actions
                that have not been confirmed.
                """

                with st.spinner("Analyzing email with AI..."):
                    response = client.responses.create(
                        model=model,
                        instructions=instructions,
                        input=email_text
                    )

                result = response.output_text

                st.success("Email analysis completed!")

                st.subheader("AI Analysis")
                st.markdown(result)

                st.download_button(
                    label="Download analysis",
                    data=result,
                    file_name="email_analysis.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            except Exception as error:
                st.error(
                    "Something went wrong while contacting "
                    "the OpenAI API."
                )
                st.code(str(error))

st.divider()

st.caption(
    "AI Mail Assistant | Python • Streamlit • OpenAI API"
)
