# SelfHealingCodeAgent
🔧 A self-healing AI agent that detects errors from logs and suggests code fixes using GPT-4
# 🤖 Self-Healing Code Agent for DevOps Automation

A smart AI-powered DevOps assistant that **monitors logs**, **detects errors**, and **suggests real-time bug fixes** using **GPT-4**. It even simulates a CI/CD pipeline by auto-generating a Pull Request with the fix.

[![Streamlit Live App](https://img.shields.io/badge/🚀%20Try%20Now-Streamlit%20App-orange?logo=streamlit)](https://selfhealingcodeagent.streamlit.app)

---

## 🌐 Live Demo

🔗 **Try it now** → ([https://selfhealingcodeagent.streamlit.app](https://selfhealingcodeagent-jt4jbp3djtau448bbrxyhj.streamlit.app/))

---

## 📁 Folder Structure

SelfHealingCodeAgent/
├── agent/ # GPT-4 based error fix logic
│ └── llm_fix_agent.py
├── cicd/ # Simulated CI/CD PR system
│ └── create_pr.py
├── logs/ # Log files to be monitored
│ └── sample_log.txt
├── monitor/ # Error detection from logs
│ └── anomaly_detector.py
├── utils/ # Helpers like log parser
│ └── parser.py
├── main.py # CLI runner for the agent
├── streamlit_app.py # Streamlit app file
├── .env.example # API key format
├── requirements.txt # Python dependencies
└── README.md # You are here

yaml
Copy
Edit

---

## 🔧 Local Setup

### ✅ Prerequisites

- Python 3.10+
- OpenAI API Key → [Get one here](https://platform.openai.com/account/api-keys)

### 📦 Installation

1. Clone this repo or download as ZIP
2. Install dependencies:

```bash
pip install -r requirements.txt
Create a .env file in root folder with your API key:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
🧪 Usage
▶️ Run in Terminal
bash
Copy
Edit
python main.py
🌐 Run with Streamlit UI
bash
Copy
Edit
streamlit run streamlit_app.py
📌 Features
🔍 Detects log anomalies like ERROR, Exception, etc.

🤖 Uses GPT-4 to suggest code-level fixes

⚙️ Simulates CI/CD flow with auto Pull Request creation

🌐 Beautiful Streamlit interface

🔐 API key management with .env

🧠 Future Enhancements
Feature	Tech Stack
Real-time monitoring	Watchdog / OpenTelemetry
Auto PR to GitHub	PyGitHub / GitHub API
Auto-testing pipeline	Pytest + GitHub Actions
Fix verification loop	Reinforcement Learning

✨ Show Some Love
If you like this project, please consider giving it a ⭐ star and sharing it with your dev friends!
Pull requests, issues, and feedback are always welcome.

👤 Author
Manisha Priya – AI Developer | DevOps Enthusiast
📧 manishapriya1325@gmail.com
