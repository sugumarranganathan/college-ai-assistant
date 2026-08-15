import vertexai
from vertexai.tuning import sft

PROJECT_ID = "gen-lang-client-0946395083"
REGION = "us-central1"

TRAIN_DATASET = (
    "gs://college-ai-assistant-788031406364/"
    "gemini_train.jsonl"
)

VALIDATION_DATASET = (
    "gs://college-ai-assistant-788031406364/"
    "gemini_validation.jsonl"
)

# Initialize Vertex AI
vertexai.init(
    project=PROJECT_ID,
    location=REGION
)

# Create the supervised fine-tuning job
tuning_job = sft.train(
    source_model="gemini-2.5-flash",
    train_dataset=TRAIN_DATASET,
    validation_dataset=VALIDATION_DATASET,
    tuned_model_display_name="college-information-ai-assistant"
)

print("\nTuning job created successfully!")
print(tuning_job)
