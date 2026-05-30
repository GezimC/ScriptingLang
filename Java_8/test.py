import hashlib
import json
from pathlib import Path

random_string = "this is random stringg"
hashed_string = hashlib.sha256(random_string.encode()).hexdigest()
print(len(hashed_string))
print(hashed_string)

result = ''
with open("important_files/config.txt", "rb") as file:
     result = hashlib.sha256(file.read()).hexdigest()

#
# json_format = {
#     "file_name" : "important_files/config.txt",
#     "hash_value" : result
# }
#
# with open("baseline.json","w") as file:
#     json.dump(json_format,file, indent=4)



base_directory = Path("important_files")


for log_file in base_directory.rglob("*"):
    print(f"Found: {log_file} ({log_file.stat().st_size} bytes)")





