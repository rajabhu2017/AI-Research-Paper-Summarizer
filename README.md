# AI-Research-Paper-Summarizer
An AI-powered web application that summarizes research papers using **Google Gemini** and **LangChain**. Users can choose a research paper, select their preferred explanation style and summary length, and receive an AI-generated summary through an interactive Streamlit interface.

## 🚀 Features

- 📄 Summarizes research papers using Google Gemini
- 🎯 Multiple explanation styles:
  - Beginner-Friendly
  - Technical
  - Code-Oriented
  - Mathematical
- 📏 Adjustable summary length:
  - Short
  - Medium
  - Long
- ⚡ Interactive Streamlit web interface
- 🔗 Prompt management using LangChain Prompt Templates

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
Research-Paper-Summarizer/
│
├── app.py
├── template.json
├── requirements.txt
├── README.md
├── .env.example
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Research-Paper-Summarizer.git

cd Research-Paper-Summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project root and add:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

You can generate an API key from Google AI Studio.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## 🧠 How It Works

1. Select a research paper.
2. Choose the explanation style.
3. Select the desired summary length.
4. LangChain formats the prompt.
5. Google Gemini generates the summary.
6. The summary is displayed in the Streamlit interface.

---

## 📸 Screenshots

Add screenshots of the application here.

Example:

```
assets/
    home_page.png
    summary_output.png
```

---

## 📌 Future Improvements

- Upload and summarize custom PDF research papers
- Question Answering (QA) on uploaded papers
- Retrieval-Augmented Generation (RAG)
- Download summaries as PDF
- Support multiple LLM providers
- Citation extraction
- Research paper comparison

---

## 📚 Learning Outcomes

This project helped me learn:

- LangChain Prompt Templates
- Google Gemini API integration
- Streamlit application development
- Environment variable management
- Prompt engineering
- Building AI-powered applications with Python

---

## 👨‍💻 Author

**Raja**

MBA Student | AI & Data Analytics Enthusiast

---

## ⭐ Acknowledgements

- LangChain
- Google Gemini
- Streamlit
