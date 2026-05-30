from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "Java_8" / "important_files"/  "config.txt"

FLAGS = ["password", "api_key"]

def scan_file(path):
    findings = []

    with open(path, 'r') as f:
        content = f.readlines()

    for index in range(len(content)):
        if "password" in content[index]:
            findings.append(
                {
                    "file": path,
                    "line": content[index].strip(),
                    "line_number": index + 1
                }
            )

    print(findings)



scan_file(FILE_PATH)
