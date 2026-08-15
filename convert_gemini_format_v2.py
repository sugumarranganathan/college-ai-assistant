import csv
import json

INPUT_FILE = "college_data_clean.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    data = list(reader)

print(f"Total examples found: {len(data)}")

# Use approximately 90% for training and 10% for validation
split_index = int(len(data) * 0.9)

train_data = data[:split_index]
validation_data = data[split_index:]

print(f"Training examples: {len(train_data)}")
print(f"Validation examples: {len(validation_data)}")


def convert_to_gemini_format(examples, output_file):
    with open(output_file, "w", encoding="utf-8") as f:

        for item in examples:

            record = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [
                            {
                                "text": item["question"]
                            }
                        ]
                    },
                    {
                        "role": "model",
                        "parts": [
                            {
                                "text": item["answer"]
                            }
                        ]
                    }
                ]
            }

            f.write(json.dumps(record) + "\n")


convert_to_gemini_format(
    train_data,
    "gemini_train_v2.jsonl"
)

convert_to_gemini_format(
    validation_data,
    "gemini_validation_v2.jsonl"
)

print("\nGemini V2 JSONL files created successfully!")
