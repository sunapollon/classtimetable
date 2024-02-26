import json
with open('your_file.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

for user in data["user"]:
    cleaned_data = [c for c in user["data"] if "className" in c and c["className"] != ""]
    user["data"] = cleaned_data

with open("result.json", 'w', encoding='utf-8-sig') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
