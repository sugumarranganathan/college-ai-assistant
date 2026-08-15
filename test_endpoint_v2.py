from google.cloud import aiplatform_v1
import json

PROJECT_ID = "788031406364"
LOCATION = "us-central1"

ENDPOINT_ID = "5349894277025497088"
DEPLOYED_MODEL_ID = "7453541495937695744"

client = aiplatform_v1.PredictionServiceClient(
    client_options={
        "api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"
    }
)

endpoint = (
    f"projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/{ENDPOINT_ID}"
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
        response = client.predict(
            endpoint=endpoint,
            instances=[
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": question
                                }
                            ]
                        }
                    ]
                }
            ],
            parameters={}
        )

        print("RAW RESPONSE:")
        print(response)

    except Exception as e:
        print("ERROR:", e)

print("\n" + "=" * 60)
print("V2 ENDPOINT TEST COMPLETED")
