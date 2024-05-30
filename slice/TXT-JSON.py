import os
import json

output_dir = 'rockyou/JSON'
os.makedirs(output_dir, exist_ok=True)

passwords_dict = {}

with open('rockyou.txt', 'r', encoding='latin-1') as file:
    for line in file:
        password = line.strip()
        length = len(password)

        if length not in passwords_dict:
            passwords_dict[length] = []

        passwords_dict[length].append(password)

for length, passwords in passwords_dict.items():
    data = {
        "passwords": passwords
    }
    output_file = os.path.join(output_dir, f'rockyou-{length}.json')
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

print("The division and saving of entries into JSON files has been completed!")
