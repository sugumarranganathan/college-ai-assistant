from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from google import genai


# --------------------------------------------------
# GOOGLE CLOUD CONFIGURATION
# --------------------------------------------------

PROJECT_ID = "gen-lang-client-0946395083"

LOCATION = "us-central1"


# --------------------------------------------------
# FINE-TUNED GEMINI V2 ENDPOINT
# --------------------------------------------------

TUNED_ENDPOINT = (
    "projects/788031406364/locations/us-central1/"
    "endpoints/5349894277025497088"
)


# --------------------------------------------------
# FASTAPI APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="Bright Future College of Engineering AI Chatbot"
)


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# --------------------------------------------------
# HTML TEMPLATES
# --------------------------------------------------

templates = Jinja2Templates(
    directory="templates"
)


# --------------------------------------------------
# GEMINI CLIENT
# --------------------------------------------------

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)


# --------------------------------------------------
# REQUEST MODEL
# --------------------------------------------------

class QuestionRequest(BaseModel):

    question: str


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.get(
    "/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# --------------------------------------------------
# ASK QUESTION API
# --------------------------------------------------

@app.post("/ask")
async def ask_question(data: QuestionRequest):

    question = data.question.strip()

    # Check if the question is empty
    if not question:

        return {
            "answer": "Please enter a question."
        }


    # --------------------------------------------------
    # COLLEGE AI ASSISTANT INSTRUCTIONS
    # --------------------------------------------------

    prompt = f"""
You are the official AI Assistant for Bright Future College of Engineering.

Your responsibility is to help students, parents, and visitors with information related ONLY to Bright Future College of Engineering.

You can answer questions about:

- College information
- Courses and departments
- Admissions
- Eligibility criteria
- Admission procedure
- Fees
- Scholarships
- Hostel facilities
- Placements
- Campus facilities
- Transport
- Faculty
- Student support
- Academic information

IMPORTANT RULES:

1. Answer only questions related to Bright Future College of Engineering.

2. Use the information you have been trained or fine-tuned on.

3. Do not provide information about unrelated topics such as:
   - React
   - useReducer
   - General programming
   - Random technology questions
   - Other unrelated subjects

4. If the user's question is unrelated to the college, respond exactly:

"I am the Bright Future College AI Assistant. Please ask me questions related to college courses, admissions, fees, hostel, placements, campus facilities, or other college-related services."

5. Keep your answers clear, helpful, and student-friendly.

Student Question:

{question}
"""


    try:

        # Send question to Fine-Tuned Gemini Model
        response = client.models.generate_content(
            model=TUNED_ENDPOINT,
            contents=prompt
        )


        return {
            "question": question,
            "answer": response.text
        }


    except Exception as e:

        return {
            "answer": f"Error: {str(e)}"
        }
