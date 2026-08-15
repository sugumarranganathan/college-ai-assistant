import csv
import json

input_file = "college_data.csv"
output_file = "input.jsonl"

with open(input_file, "r", encoding="utf-8") as csv_file, \
     open(output_file, "w", encoding="utf-8") as jsonl_file:

    reader = csv.DictReader(csv_file)

    for row in reader:
        data = {
            "input": row["question"],
            "output": row["answer"]
        }

        jsonl_file.write(json.dumps(data) + "\n")

print(f"Successfully created {output_file}")
