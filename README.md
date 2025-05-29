# 🤖 SmartBot PDF Assistant

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Gemini AI](https://img.shields.io/badge/Powered%20By-Gemini%20AI-blue?logo=google)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/github/license/vansh-121/SmartBot-PDF-Assistant)](LICENSE)
[![Project Status: Active – Maintained and usable](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/vansh-121/SmartBot-PDF-Assistant)

---

## 🌐 Live App

👉 Try it here: [smartbot-pdf-ai.streamlit.app](https://smartbot-pdf-ai.streamlit.app/) 

*(Press **Yes, get this app backup!** & wait for a few seconds — due to free tier CPU limitations)*

---

## 📘 Overview

**SmartBot PDF Assistant** is an AI-powered PDF Q&A tool built using **Streamlit** and **Gemini** (Google’s state-of-the-art large language model). It allows users to interact with PDF documents in a conversational manner — upload your file, ask anything about it, and get accurate responses derived directly from the content.

---

## ⚡ Features

- 📄 Upload and preview PDF documents
- 💬 Ask context-based questions about the uploaded PDF
- 🤖 AI responses powered by **Gemini** via Vertex AI or PaLM API
- 🧠 Maintains context during session for coherent conversations
- 🔐 No data stored – privacy-first approach
- 🌐 Web-based and accessible on any device

---

## 🔧 Built With

| Tool/Tech         | Role                                  |
|-------------------|----------------------------------------|
| **Streamlit**     | UI framework for Python web apps       |
| **Gemini API**    | AI model for answering PDF questions   |
| **PyMuPDF / PyPDF2** | PDF parsing and text extraction   |
| **Python**        | Core application logic and backend     |

---

## 📸 Screenshots

> _Coming Soon: UI snapshots and GIF demo_

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/vansh-121/SmartBot-PDF-Assistant.git
cd SmartBot-PDF-Assistant
```

### 2. Set Up Environment
Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API
Set your Gemini/PaLM API key using an .env file:

```bash
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run app.py
```

---

#### Made with ❤️ by Vansh

