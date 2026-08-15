from google import genai

PROJECT_ID = "gen-lang-client-0946395083"
LOCATION = "us-central1"

TUNED_ENDPOINT = (
    "projects/788031406364/locations/us-central1/"
    "endpoints/5349894277025497088"
)

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

response = client.models.generate_content(
    model=TUNED_ENDPOINT,
    contents="What is the name of the college?"
)

print(response.text)
