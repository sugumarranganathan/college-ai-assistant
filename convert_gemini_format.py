import json

def convert(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            data = json.loads(line)

            gemini_data = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [
                            {
                                "text": data["input"]
                            }
                        ]
                    },
                    {
                        "role": "model",
                        "parts": [
                            {
                                "text": data["output"]
                            }
                        ]
                    }
                ]
            }

            outfile.write(json.dumps(gemini_data) + "\n")


convert("input.jsonl", "gemini_train.jsonl")
convert("evaluation.jsonl", "gemini_validation.jsonl")

print("Gemini JSONL files created successfully.")
