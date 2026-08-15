from google import genai
from google.genai.types import HttpOptions

PROJECT_ID = "788031406364"
LOCATION = "us-central1"

MODEL_ID = "projects/788031406364/locations/us-central1/models/3808761604930011136@1"

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
    http_options=HttpOptions(api_version="v1")
)

questions = [
    "What is the name of the college?",
    "Where is the college located?",
    "What engineering branches are available?",
    "Is hostel accommodation available?",
    "Does the college provide placement assistance?",
    "Does the college provide transport facilities?",
    "What facilities are available for students?",
    "How can I get admission information?",
    "Does the college have a library?",
    "What support is available for students?"
]

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=question
        )

        print("ANSWER:", response.text)

    except Exception as e:
        print("ERROR:", e)

print("\n" + "=" * 60)
print("V2 TUNED MODEL TEST COMPLETED")
