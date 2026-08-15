# 🎓 Bright Future College AI Chatbot

## 🤖 AI & Technologies Used

**Fine-Tuned Gemini 2.5 Flash | Vertex AI | FastAPI | Python | HTML | CSS | JavaScript | Docker | Google Cloud Run**

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

# Key Features

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


🔄 How It Works
1️⃣ User asks a question

The user enters a question through the chatbot interface.

Example:

What courses are available?
2️⃣ Question is sent to FastAPI

The frontend sends the user's question to the FastAPI backend using an API request.

POST /ask
3️⃣ FastAPI communicates with Vertex AI

The backend sends the question to the Fine-Tuned Gemini model using the Google Gen AI SDK.

4️⃣ Fine-Tuned AI model generates a response

The Gemini model processes the question based on the information used during fine-tuning.

5️⃣ Response is displayed

The generated response is returned to the FastAPI backend and displayed in the chatbot interface.

🧠 AI Model

This project uses:

Fine-Tuned Gemini 2.5 Flash

The model is deployed and accessed through:

Google Vertex AI
Google Gen AI SDK

The fine-tuned model helps the chatbot provide responses related specifically to the college information provided during the training process.

🛠️ Technology Stack
Backend
Python
FastAPI
Uvicorn
Pydantic
AI
Google Gemini 2.5 Flash
Fine-Tuning
Google Vertex AI
Google Gen AI SDK
Frontend
HTML
CSS
JavaScript
Cloud Deployment
Google Cloud Platform
Google Cloud Run
Cloud Build
Artifact Registry
Version Control
Git
GitHub


📁 Project Structure

college-ai-assistant/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── college_data.csv
├── college_data_clean.csv
│
├── input.jsonl
├── gemini_train.jsonl
├── gemini_validation.jsonl
│
├── convert_to_jsonl.py
├── convert_gemini_format.py
├── start_tuning.py
│
└── test_tuned_model.py

=========

# 🔄 Complete Project Workflow

The **Bright Future College AI Chatbot** consists of two major workflows:

1. **Fine-Tuning the Gemini Model**
2. **Using the Fine-Tuned Model in the AI Chatbot**

---

# 🧠 1. Fine-Tuning Workflow

The Fine-Tuning process helps customize the Gemini model using college-specific information.

```text
        College Information
               │
               ▼
     ┌──────────────────────┐
     │   college_data.csv   │
     │                      │
     │ Courses              │
     │ Admissions           │
     │ Hostel               │
     │ Placements           │
     │ Campus Facilities    │
     └──────────────────────┘
               │
               ▼
     ┌──────────────────────┐
     │   Data Cleaning      │
     │                      │
     │ college_data_clean   │
     │        .csv          │
     └──────────────────────┘
               │
               ▼
     ┌──────────────────────┐
     │ Data Format          │
     │ Conversion           │
     │                      │
     │ Python Scripts       │
     └──────────────────────┘
               │
               ▼
     ┌──────────────────────┐
     │ Training Dataset     │
     │                      │
     │ gemini_train.jsonl   │
     └──────────────────────┘
               │
               ▼
     ┌──────────────────────┐
     │ Validation Dataset   │
     │                      │
     │gemini_validation.jsonl│
     └──────────────────────┘
               │
               ▼
     ┌─────────────────────────────┐
     │     Vertex AI / Gemini      │
     │                             │
     │   Base Gemini 2.5 Flash     │
     └─────────────────────────────┘
               │
               ▼
     ┌─────────────────────────────┐
     │       Fine-Tuning Job       │
     │                             │
     │  start_tuning.py            │
     │  start_tuning_v2.py         │
     └─────────────────────────────┘
               │
               ▼
     ┌─────────────────────────────┐
     │   Fine-Tuned Gemini Model   │
     │                             │
     │ College-Specific Knowledge  │
     └─────────────────────────────┘
               │
               ▼
     ┌─────────────────────────────┐
     │        Model Endpoint       │
     │                             │
     │ Vertex AI Endpoint          │
     └─────────────────────────────┘

===========

🔁 End-to-End Project Workflow

This diagram shows the complete journey from college data to the deployed AI chatbot.

                    COLLEGE DATA
                         │
                         ▼
              ┌─────────────────────┐
              │  college_data.csv   │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Data Cleaning     │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Dataset Conversion  │
              │   CSV → JSONL       │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Training Dataset    │
              │ Validation Dataset  │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Gemini 2.5       │
              │    Flash Model      │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Fine-Tuning Job   │
              │    Vertex AI        │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Fine-Tuned Gemini   │
              │       Model         │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Vertex AI Endpoint  │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   FastAPI Backend   │
              │      main.py        │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Chatbot Frontend   │
              │ HTML + CSS + JS     │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │      Docker         │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Cloud Build      │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Artifact Registry   │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Cloud Run        │
              └─────────────────────┘
                         │
                         ▼
                    👨‍🎓 USERS

========
Complete Flow in Simple Steps

College Information
        ↓
Create Dataset
        ↓
Clean Dataset
        ↓
Convert Dataset to Gemini Format
        ↓
Create Training + Validation Data
        ↓
Fine-Tune Gemini 2.5 Flash
        ↓
Create Fine-Tuned Model Endpoint
        ↓
Integrate Endpoint with FastAPI
        ↓
Connect FastAPI with Chatbot UI
        ↓
Containerize Using Docker
        ↓
Deploy Using Cloud Build
        ↓
Store Container in Artifact Registry
        ↓
Deploy Application to Cloud Run
        ↓
Users Access AI Chatbot

===========

👨‍💻 Developer

**R. Ssugumar, M.B.A**
📧 Email: contact.sugumarai@gmail.com
