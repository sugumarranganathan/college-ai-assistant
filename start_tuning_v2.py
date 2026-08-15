import vertexai
from vertexai.tuning import sft

PROJECT_ID = "gen-lang-client-0946395083"
REGION = "us-central1"

vertexai.init(
    project=PROJECT_ID,
    location=REGION
)

print("Creating Gemini 2.5 Flash V2 Supervised Tuning Job...")

tuning_job = sft.train(
    source_model="gemini-2.5-flash",
    train_dataset="gs://college-ai-assistant-788031406364/gemini_train_v2.jsonl",
    validation_dataset="gs://college-ai-assistant-788031406364/gemini_validation_v2.jsonl",
    tuned_model_display_name="college-information-ai-assistant-v2",
    epochs=40,
    adapter_size=4,
    learning_rate_multiplier=5.0
)

print("\nTuning Job V2 created successfully!")
print(tuning_job)
