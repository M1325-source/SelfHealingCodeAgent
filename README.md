# 🔧 Self-Healing Code Agent

An intelligent AI-powered DevOps assistant that automatically monitors application logs, detects errors in real-time, and suggests code-level fixes using GPT-4. The system simulates a complete CI/CD pipeline by auto-generating Pull Requests with proposed fixes.

[![GitHub Pages](https://img.shields.io/badge/demo-live-success)](https://m1325-source.github.io/SelfHealingCodeAgent/)
[![Python](https://img.shields.io/badge/python-100%25-blue)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/M1325-source/SelfHealingCodeAgent)](https://github.com/M1325-source/SelfHealingCodeAgent/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [API Configuration](#api-configuration)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)

---

## 🎯 Overview

The **Self-Healing Code Agent** revolutionizes DevOps workflows by automating the error detection and resolution process. Instead of manually monitoring logs and debugging issues, this AI agent:

1. **Monitors** application logs in real-time
2. **Detects** errors, exceptions, and anomalies automatically
3. **Analyzes** the error context using GPT-4
4. **Generates** code-level fixes with explanations
5. **Creates** Pull Requests with the proposed solution
6. **Simulates** a complete CI/CD pipeline workflow

**Perfect for:** DevOps engineers, SREs, development teams, and anyone managing production systems who want to reduce MTTR (Mean Time To Resolution) and automate incident response.

---

## ✨ Key Features

### 🔍 Intelligent Log Monitoring
- Real-time log file monitoring and parsing
- Pattern-based anomaly detection (ERROR, Exception, FATAL, etc.)
- Contextual error extraction with surrounding log lines
- Support for multiple log formats and sources

### 🤖 AI-Powered Error Analysis
- GPT-4 integration for intelligent code analysis
- Root cause identification from error messages
- Context-aware fix generation
- Code explanation and best practices suggestions

### ⚙️ Automated CI/CD Workflow
- Simulated Pull Request creation with fix details
- Pre-commit validation and testing hooks
- Integration-ready for GitHub/GitLab APIs
- Automated fix verification pipeline

### 🌐 User-Friendly Interface
- Beautiful Streamlit web dashboard
- Real-time error display and fix suggestions
- Interactive PR preview and management
- CLI support for automation and scripting

### 🔐 Secure & Configurable
- Environment-based API key management
- Configurable error detection thresholds
- Custom log pattern support
- Easy integration with existing systems

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Log Sources Layer                         │
│        (Application Logs, System Logs, Error Logs)           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Log Monitor Module                          │
│              (monitor/anomaly_detector.py)                   │
│   • Real-time log watching                                   │
│   • Pattern matching (ERROR, Exception, FATAL)               │
│   • Error extraction with context                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Parser Module                             │
│                  (utils/parser.py)                           │
│   • Log line parsing and structuring                         │
│   • Timestamp and severity extraction                        │
│   • Context aggregation                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  AI Fix Agent Module                         │
│               (agent/llm_fix_agent.py)                       │
│   • GPT-4 API integration                                    │
│   • Error analysis and root cause detection                  │
│   • Code fix generation with explanations                    │
│   • Best practices recommendations                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  CI/CD Automation Module                     │
│                  (cicd/create_pr.py)                         │
│   • Pull Request generation                                  │
│   • Fix documentation and formatting                         │
│   • Pre-commit hooks simulation                              │
│   • Integration with GitHub/GitLab APIs                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  User Interface Layer                        │
│        (streamlit_app.py / main.py CLI)                      │
│   • Dashboard visualization                                  │
│   • Interactive fix review                                   │
│   • PR management                                            │
│   • Configuration settings                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **AI/ML** | OpenAI GPT-4 | Intelligent error analysis and fix generation |
| **Backend** | Python 3.10+ | Core application logic |
| **Web UI** | Streamlit | Interactive dashboard and visualization |
| **Log Processing** | Python Logging, Regex | Pattern matching and parsing |
| **CI/CD** | Custom Python Scripts | PR generation and automation |
| **API Management** | python-dotenv | Secure environment variable handling |
| **Development** | Dev Containers | Consistent development environment |

### Key Dependencies

```
openai>=1.0.0           # GPT-4 API integration
streamlit>=1.28.0       # Web interface
python-dotenv>=1.0.0    # Environment management
watchdog>=3.0.0         # File system monitoring (optional)
requests>=2.31.0        # HTTP requests
```

---

## 📸 Screenshots

### 🖥️ Streamlit Dashboard
*(Interactive web interface showing real-time error detection and AI-generated fixes)*

### 📊 Error Detection View
*(Log monitoring with highlighted errors and anomalies)*

### 🔧 Fix Suggestion Panel
*(GPT-4 generated code fixes with explanations)*

### 📝 Pull Request Preview
*(Auto-generated PR with fix details ready for review)*

---

## 📂 Project Structure

```
SelfHealingCodeAgent/
│
├── agent/                          # AI Agent Core
│   └── llm_fix_agent.py           # GPT-4 integration for fix generation
│
├── cicd/                           # CI/CD Automation
│   └── create_pr.py               # Pull Request creation logic
│
├── logs/                           # Log Storage
│   └── sample_log.txt             # Example log file for testing
│
├── monitor/                        # Error Detection
│   └── anomaly_detector.py        # Log monitoring and pattern matching
│
├── utils/                          # Helper Utilities
│   └── parser.py                  # Log parsing and structuring
│
├── docs/                           # Documentation & Demo
│   └── index.html                 # GitHub Pages landing page
│
├── .devcontainer/                  # Development Container
│   └── devcontainer.json          # VS Code dev container config
│
├── main.py                         # CLI Entry Point
├── streamlit_app.py               # Web UI Entry Point
├── requirements.txt               # Python Dependencies
├── .env.example                   # Environment Variable Template
├── .gitignore                     # Git Ignore Rules
└── README.md                       # Project Documentation
```

---

## 🚀 Installation

### Prerequisites

- **Python 3.10 or later**
- **OpenAI API Key** → [Get one here](https://platform.openai.com/api-keys)
- **Git** (for cloning the repository)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/M1325-source/SelfHealingCodeAgent.git
cd SelfHealingCodeAgent
```

#### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# On Windows: notepad .env
# On macOS/Linux: nano .env
```

Add the following to your `.env` file:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

#### 5. Verify Installation

```bash
python -c "import streamlit; print('Setup complete!')"
```

---

## 🧪 Usage

### Option 1: Command Line Interface (CLI)

Run the agent in terminal mode for automation and scripting:

```bash
python main.py
```

**Features:**
- Monitors `logs/sample_log.txt` by default
- Detects errors automatically
- Prints AI-generated fixes to console
- Simulates PR creation

**Custom Log File:**
```bash
python main.py --log-file /path/to/your/logfile.log
```

### Option 2: Streamlit Web Dashboard

Launch the interactive web interface:

```bash
streamlit run streamlit_app.py
```

**Access the dashboard:**
- Local URL: `http://localhost:8501`
- Network URL: Check terminal output for external access

**Dashboard Features:**
- 📊 Real-time log monitoring visualization
- 🔍 Error detection with highlighting
- 🤖 AI fix suggestions with explanations
- 📝 PR preview and download
- ⚙️ Configuration settings

### Option 3: Dev Container (VS Code)

For a consistent development environment:

1. Open the project in VS Code
2. Install the "Remote - Containers" extension
3. Press `F1` → Select "Reopen in Container"
4. The environment will be set up automatically

---

## 🔬 How It Works

### Workflow Overview

```
Step 1: Log Monitoring
┌─────────────────────────────────────────┐
│  Monitor watches log files for changes  │
│  Detects patterns: ERROR, Exception     │
└─────────────┬───────────────────────────┘
              ▼
Step 2: Error Detection
┌─────────────────────────────────────────┐
│  Anomaly detector extracts error lines  │
│  Captures context (5 lines before/after)│
└─────────────┬───────────────────────────┘
              ▼
Step 3: AI Analysis
┌─────────────────────────────────────────┐
│  GPT-4 analyzes error with context      │
│  Generates code-level fix suggestion    │
│  Provides explanation and best practices│
└─────────────┬───────────────────────────┘
              ▼
Step 4: PR Creation
┌─────────────────────────────────────────┐
│  Format fix as Pull Request             │
│  Include error details, fix, and tests  │
│  Simulate CI/CD pipeline approval       │
└─────────────────────────────────────────┘
```

### Example Scenario

**1. Log Entry Detected:**
```
2026-02-04 10:30:45 ERROR [DatabaseConnection] Connection timeout after 30s
```

**2. AI Analysis:**
```
Root Cause: Database connection pool exhausted
Recommended Fix: Increase pool size and add connection retry logic
```

**3. Generated Fix:**
```python
# Before
db_pool = create_pool(max_connections=10)

# After (AI-suggested fix)
db_pool = create_pool(
    max_connections=50,
    timeout=60,
    retry_on_timeout=True,
    max_retries=3
)
```

**4. Pull Request Created:**
```
Title: [AutoFix] Resolve database connection timeout
Description: Increased connection pool size and added retry logic
Files Changed: database/connection.py
Status: Ready for Review
```

---

## 🔐 API Configuration

### OpenAI API Setup

1. **Get Your API Key:**
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy the key (it starts with `sk-`)

2. **Set Up Environment:**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=sk-your-key-here" > .env
   ```

3. **Verify Configuration:**
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   api_key = os.getenv("OPENAI_API_KEY")
   print("API configured!" if api_key else "API key missing!")
   ```

### Cost Optimization Tips

- Use GPT-4 for complex errors, GPT-3.5 for simple ones
- Cache similar error patterns to avoid redundant API calls
- Set rate limits to control costs
- Monitor usage on OpenAI dashboard

---

## 🔮 Future Enhancements

### Roadmap

| Feature | Tech Stack | Status | Priority |
|---------|-----------|--------|----------|
| **Real-time log monitoring** | Watchdog / OpenTelemetry | 🔄 In Progress | High |
| **Auto PR to GitHub** | PyGitHub / GitHub API | 📋 Planned | High |
| **Automated testing pipeline** | Pytest + GitHub Actions | 📋 Planned | High |
| **Fix verification loop** | Reinforcement Learning | 🔬 Research | Medium |
| **Multi-source log aggregation** | ELK Stack integration | 📋 Planned | Medium |
| **Slack/Teams notifications** | Webhook integration | 📋 Planned | Low |
| **Custom ML models** | TensorFlow / PyTorch | 🔬 Research | Low |
| **Dashboard analytics** | Plotly / Chart.js | 📋 Planned | Medium |

### Phase 1: Enhanced Monitoring (Q2 2026)
- [ ] Real-time file watching with Watchdog
- [ ] Support for multiple log sources
- [ ] Custom error pattern configuration
- [ ] Integration with OpenTelemetry

### Phase 2: GitHub Integration (Q3 2026)
- [ ] Actual GitHub PR creation via API
- [ ] Automated branch creation and commits
- [ ] PR review automation
- [ ] Integration with GitHub Actions

### Phase 3: Testing & Validation (Q3 2026)
- [ ] Automated test generation for fixes
- [ ] Fix verification before PR creation
- [ ] Rollback mechanism for failed fixes
- [ ] Integration testing pipeline

### Phase 4: Advanced AI (Q4 2026)
- [ ] Reinforcement learning for fix quality improvement
- [ ] Multi-model ensemble for better accuracy
- [ ] Custom fine-tuned models for specific codebases
- [ ] Predictive error detection

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/SelfHealingCodeAgent.git
   cd SelfHealingCodeAgent
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make Your Changes**
   - Add new features
   - Fix bugs
   - Improve documentation
   - Add tests

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Describe your changes clearly

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to all functions and classes
- Include unit tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

### Areas for Contribution

- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **New Features**: Implement items from the roadmap
- 📝 **Documentation**: Improve README, add tutorials
- 🧪 **Testing**: Add unit tests and integration tests
- 🎨 **UI/UX**: Enhance Streamlit dashboard
- 🔧 **DevOps**: Improve CI/CD, Docker support

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Manisha Priya**  
AI Developer | DevOps Enthusiast | Automation Architect

Passionate about building intelligent systems that make developers' lives easier.

- 📧 Email: [manishapriya1325@gmail.com](mailto:manishapriya1325@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
- 🐙 GitHub: [@M1325-source](https://github.com/M1325-source)
- 🌐 Website: [m1325-source.github.io/SelfHealingCodeAgent](https://m1325-source.github.io/SelfHealingCodeAgent/)

---

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4 API
- Streamlit team for the amazing framework
- The DevOps and SRE communities for inspiration
- All contributors and supporters of this project

---

## 📞 Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/M1325-source/SelfHealingCodeAgent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/M1325-source/SelfHealingCodeAgent/discussions)
- **Email**: manishapriya1325@gmail.com

### FAQ

**Q: How much does it cost to run?**  
A: Costs depend on OpenAI API usage. Typical usage: ~$0.01-0.05 per error analysis.

**Q: Can I use this with private repositories?**  
A: Yes! Configure GitHub Personal Access Token in `.env` for private repo access.

**Q: Does it work with languages other than Python?**  
A: Yes! The AI can suggest fixes for any language in your logs.

**Q: How accurate are the fixes?**  
A: GPT-4 provides high-quality suggestions, but always review before applying.

---

## ⭐ Show Your Support

If you find this project useful:

- ⭐ **Star the repository** on GitHub
- 🍴 **Fork it** and build something awesome
- 📢 **Share it** with your dev friends and colleagues
- 💬 **Provide feedback** through issues or discussions
- 🤝 **Contribute** by submitting PRs

**Every star motivates me to keep improving this project!**

---

## 📊 Project Stats

- 🌟 **3 Stars** (and growing!)
- 🔄 **10 Deployments** on GitHub Pages
- 💻 **100% Python** codebase
- 📦 **14 Commits** of continuous improvement

---

## 🎥 Demo

**Live Demo:** [View on GitHub Pages](https://m1325-source.github.io/SelfHealingCodeAgent/)

**Video Demo:** Check out `Self-Healing-DevOps-Demo.mp4` in the repository for a full walkthrough!

---

**Built with ❤️ by Manisha Priya**

*Making DevOps smarter, one automated fix at a time.*

---

*Last Updated: February 2026*
