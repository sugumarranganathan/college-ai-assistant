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
            model=TUNED_ENDPOINT,
            contents=question,
        )

        print("ANSWER:", response.text)

    except Exception as e:
        print("ERROR:", e)


print("\n" + "=" * 60)
print("V2 TUNED MODEL TEST COMPLETED")
