import json as js
import hashlib as hl
from pathlib import Path

def read_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    return content


def calculate_file_hash(file_path):
    content = read_file(file_path)
    file_hash = hl.sha256(content).hexdigest()  #document sign
    return file_hash

def scan_folder(folder_path):
    files_hash = {}

    for file_path in Path(folder_path).rglob("*"):
        hash = calculate_file_hash(file_path)
        files_hash[str(file_path)] = hash
    return files_hash


def create_baseline(folder_path):
    files_hash = scan_folder(folder_path)

    with open("baseline.json", "w") as f:
        js.dump(files_hash, f, indent=4)

    print("baseline.json created")


def load_baseline():
    with open("baseline.json", "r") as f:
        return js.load(f)


def print_baseline():
    file = load_baseline()
    print(file)


def check_integrity(folder_path):
    current_hashes = scan_folder(folder_path)  #new dictioniary
    previous_hashes = load_baseline()

    for file_name in current_hashes.keys():
        if file_name in previous_hashes:
            if previous_hashes[file_name] != current_hashes[file_name]:
                print("File change: ", file_name)
        else:
            print("New file add: ", file_name)


def main():

    while True:
        user_choice = input("Select option:, \n1. Create baseline, \n2. Load baseline, \n3. Check integrity, \n4. Exit: ")

        if user_choice == "1":
            create_baseline("important_files")
        elif user_choice == "2":
            print_baseline()
        elif user_choice == "3":
            check_integrity("important_files")
        elif user_choice == "4":
            exit()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()





# calculate_file_hash(file_path) -> returns SHA256 hash of one file
# scan_folder(folder_path) -> returns dictionary with file paths and their hashes
# create_baseline(folder_path) -> creates baseline.json from current files
# load_baseline(folder_path) -> loads and returns saved baseline.json
# check_integrity(folder_path) -> compares current files with baseline and shows results
# show_menu() -> prints menu options
# main() -> runs the program menu loop