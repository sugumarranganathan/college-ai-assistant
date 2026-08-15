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


# Fine-Tuned Gemini V2 Endpoint

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

    if not question:

        return {
            "answer": "Please enter a question."
        }


    try:

        response = client.models.generate_content(
            model=TUNED_ENDPOINT,
            contents=question
        )


        return {
            "question": question,
            "answer": response.text
        }


    except Exception as e:

        return {
            "answer": f"Error: {str(e)}"
        }
