from google import genai

PROJECT_ID = "gen-lang-client-0946395083"
LOCATION = "us-central1"

TUNED_ENDPOINT = (
    "projects/788031406364/locations/us-central1/"
    "endpoints/8237546063100116992"
)

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

questions = [
    "What is the name of the college?",
    "Where is the college located?",
    "What engineering branches are available?",
    "Is hostel accommodation available?",
    "Does the college provide placement assistance?"
]

for question in questions:
    response = client.models.generate_content(
        model=TUNED_ENDPOINT,
        contents=question,
    )

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("ANSWER:", response.text)
