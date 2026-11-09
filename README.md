# 📧 AI Mail Assistant

An AI-powered email analysis tool that helps customer support teams understand incoming customer messages, identify priorities, and generate professional reply drafts.

**Built with Python, Streamlit, and the OpenAI API.**

<p align="center">
  <a href="https://ai-mail-assistant-jo9mbetm5vux4e7jkqhld9.streamlit.app/">
    <strong>🚀 Try the Live Demo</strong>
  </a>
  &nbsp; | &nbsp;
  <a href="https://github.com/moseskakuno/ai-mail-assistant">
    <strong>View Source Code</strong>
  </a>
</p>

---

## 🎯 Project Overview

Customer support teams often receive a large number of emails covering different topics, priorities, and customer concerns.

Manually reviewing and responding to every message can be time-consuming.

The **AI Mail Assistant** demonstrates how generative AI can support this workflow by analyzing customer emails and producing structured, actionable insights.

Users can paste an incoming email into the application and receive an AI-generated analysis together with a professional reply draft.

The goal is to make email handling faster, more structured, and more efficient while keeping a human in control of the final response.

## ✨ Features

The application currently provides the following capabilities:

- **Email Categorization** – Identifies the main topic of an incoming customer email, such as order status or delivery delays.
- **Priority Detection** – Classifies customer requests as Low, Medium, or High priority.
- **Sentiment Analysis** – Identifies whether the customer's tone is Positive, Neutral, or Negative.
- **Email Summarization** – Generates a concise summary of the customer's request.
- **Recommended Next Steps** – Suggests practical actions for handling the request.
- **AI Reply Generation** – Creates a professional reply draft in the language of the original email.
- **Download Analysis** – Allows users to download the generated analysis as a text file.

## 🖥️ Live Demo

Try the application here:

👉 https://ai-mail-assistant-jo9mbetm5vux4e7jkqhld9.streamlit.app/

**Example workflow:**

1. Paste a customer email into the text area.
2. Click **Analyze Email**.
3. Wait for the AI to process the message.
4. Review the category, priority, sentiment, summary, and recommended next steps.
5. Review the generated reply draft.
6. Download the analysis if needed.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| OpenAI API | AI-powered email analysis and reply generation |
| python-dotenv | Local environment variable management |
| Git & GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment |

## 🏗️ Project Structure

```text
ai-mail-assistant/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Local API credentials (not committed)
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to run the application locally.

### 1. Clone the repository

```bash
git clone https://github.com/moseskakuno/ai-mail-assistant.git

cd ai-mail-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your OpenAI API key

Create a `.env` file in the project root directory:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=your_available_api_model
```

Replace the placeholders with your own OpenAI API credentials and an API model available to your account.

**Important:** Never commit your API key to GitHub. The `.env` file is excluded through `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud** and connected to this GitHub repository.

To deploy your own instance:

1. Fork or clone this repository.
2. Connect your GitHub account to Streamlit Community Cloud.
3. Select the repository and `app.py` as the main file.
4. Add your API credentials under **App Settings → Secrets**.

Configure your secrets using TOML format:

```toml
OPENAI_API_KEY = "your_openai_api_key"
OPENAI_MODEL = "your_available_api_model"
```

Streamlit Cloud securely provides these secrets to the application at runtime.

## 🔐 Security & Responsible AI Usage

- API credentials are stored in environment variables or Streamlit Secrets.
- API keys are not included in the public repository.
- AI-generated content should be reviewed by a human before being used in customer communication.
- The application generates reply drafts but does not automatically send emails.
- Users should avoid submitting sensitive personal or confidential customer information unless they are authorized to do so.

## 🚧 Future Improvements

Potential next development steps include:

- Improved dashboard and user interface.
- One-click copying of generated reply drafts.
- More advanced email classification.
- Additional language support.
- Integration with email services.
- Structured analysis results and reporting.
- Automated customer support workflows.

## 💡 What I Learned

Building this project provided practical experience with:

- Integrating the OpenAI API into a Python application.
- Building an interactive web application with Streamlit.
- Managing API credentials securely using environment variables and Streamlit Secrets.
- Handling AI-generated responses in an application workflow.
- Using Git and GitHub for version control.
- Deploying a Python application to Streamlit Community Cloud.

## 👨‍💻 Author

**Moses Ochieng Akuno**

Web Developer | Python | JavaScript | AI Application Development

GitHub: https://github.com/moseskakuno/ai-mail-assistant

A portfolio project demonstrating practical applications of:

- Generative AI
- OpenAI API Integration
- Email Classification and Categorization
- Priority Detection and Sentiment Analysis
- AI-Powered Text Summarization
- Automated Reply Drafting
- Python Application Development
- Interactive Web Applications with Streamlit

---

*This project was developed as a practical demonstration of Python development, API integration, and applied generative AI.*