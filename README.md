# 🎓 Bright Future College AI Chatbot

An AI-powered college information assistant designed to provide quick and intelligent answers about **Bright Future College of Engineering**.

The chatbot helps students and visitors get information about courses, admissions, hostel facilities, placements, campus facilities, transport, and other college-related services.

The application uses a **Fine-Tuned Gemini 2.5 Flash model** through **Vertex AI** and is deployed on **Google Cloud Run**.

---

## 🌐 Live Application

**Live Demo:**

https://bright-future-college-ai-788031406364.us-central1.run.app

---

#  Problem Statement

Students and parents often need information about a college before applying for admission.

They may have questions such as:

- What courses are available?
- What is the admission process?
- Does the college provide hostel facilities?
- Is placement assistance available?
- What campus facilities are provided?
- How many students were placed last year?
- Is transport available?

Traditionally, students need to search through websites, brochures, or contact college staff to find answers.

This process can be time-consuming and may not provide instant responses.

Therefore, there is a need for an intelligent system that can provide **quick, interactive, and accurate college-related information through a conversational interface**.

---

#  Solution

The **Bright Future College AI Chatbot** provides an AI-powered conversational solution for answering college-related questions.

A Fine-Tuned Gemini model is trained using college information and is integrated with a FastAPI backend.

Users can ask questions through a simple chatbot interface.

The system processes the user's question and generates a relevant response using the Fine-Tuned Gemini model deployed through Vertex AI.

This helps students and parents access college information quickly without manually searching through multiple sources.

---

# ✨Key Features

- 🤖 AI-powered college information chatbot
- 🎓 Provides information about the college
- 📚 Course and program information
- 📝 Admission-related information
- 💼 Placement support information
- 🏠 Hostel information
- 🏫 Campus facilities information
- 🚌 Transport and student support information
- ⚡ Quick question buttons
- 💬 Interactive chatbot interface
- 🧠 Fine-Tuned Gemini 2.5 Flash model
- ☁️ Vertex AI integration
- 🚀 Deployed using Google Cloud Run
- 📱 Responsive web interface

---

# 🏗️ System Architecture

```text
                USER
                  │
                  ▼
        ┌───────────────────┐
        │   Web Interface   │
        │ HTML / CSS / JS   │
        └───────────────────┘
                  │
                  ▼
        ┌───────────────────┐
        │     FastAPI       │
        │      Backend      │
        └───────────────────┘
                  │
                  ▼
        ┌───────────────────┐
        │    Vertex AI      │
        │                   │
        │ Fine-Tuned Gemini │
        │   2.5 Flash       │
        └───────────────────┘
                  │
                  ▼
        ┌───────────────────┐
        │   AI Response     │
        └───────────────────┘
                  │
                  ▼
                USER
