import json
import os
import sys

def convert(jsonl_file: str, dataset_name: str):
    with open(jsonl_file, "r") as f:
        jsonl_data = f.readlines()
        jsonl_data = [json.loads(x.strip()) for x in jsonl_data]

    result = []

    for item in jsonl_data:
        if not item["answer"]:
            continue

        if "python" not in item["answer"]:
            continue

        slug = item["slug"]
        title = item["title"]

        if "difficulty" not in item:
            item["difficulty"] = "Unknown"

        difficulty = item["difficulty"]
        content = item["content"]

        
        answer = item["answer"]["python"]
        explanation = item["answer"]["explanation"]
        
        slug = "# " + slug + "\n"
        title = "# " + title + "\n"
        difficulty = "# " + difficulty + "\n"
        content = "# " + content + "\n"
        explanation = "# " + explanation + "\n"
        answer = answer + "\n"

        code_with_data = slug + title + difficulty + content + answer + explanation
        code_only = answer

        result.append({"id": item["id"], "code_with_data": code_with_data, "code_only": code_only})

    # store result to json file
    with open(dataset_name + ".json", "w") as f:
        json.dump(result, f, indent=4)


if __name__ == "__main__":
    dataset_name = "leetcode-solutions"
    convert("../leetcode-solutions.jsonl", dataset_name)

