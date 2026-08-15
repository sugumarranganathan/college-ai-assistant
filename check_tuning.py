import vertexai
from vertexai.tuning import sft

PROJECT_ID = "gen-lang-client-0946395083"
REGION = "us-central1"

TUNING_JOB_NAME = (
    "projects/788031406364/locations/us-central1/"
    "tuningJobs/7256965593033605120"
)

vertexai.init(
    project=PROJECT_ID,
    location=REGION
)

tuning_job = sft.SupervisedTuningJob(TUNING_JOB_NAME)

print("Tuning Job State:")
print(tuning_job.state)

print("\nJob Information:")
print(tuning_job)
