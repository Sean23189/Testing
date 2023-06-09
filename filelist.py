import os
from pathlib import Path

class Counters:
    def __init__(self):
        self.files = 0
        self.directories = 0
        self.inaccessible = 0

def list_files(path, indentation='', counters=None):
    try:
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                print(f'{indentation}|- {item}')
                counters.files += 1
            elif os.path.isdir(item_path):
                print(f'{indentation}|+ {item}')
                counters.directories += 1
                list_files(item_path, indentation + '|  ', counters)
    except PermissionError:
        print(f'{indentation}|! Permission denied: {Path(path).resolve()}')
        counters.inaccessible += 1

def main():
    root_directory = input("Enter the root directory path: ")
    root_directory = root_directory.strip()

    if not os.path.isdir(root_directory):
        print(f'Error: "{root_directory}" is not a valid directory.')
        return

    print(f'Listing all files and directories in: {Path(root_directory).resolve()}\n')
    counters = Counters()
    list_files(root_directory, counters=counters)

    print("\nSummary:")
    print(f"Files: {counters.files}")
    print(f"Directories: {counters.directories}")
    print(f"Inaccessible: {counters.inaccessible}")

if __name__ == '__main__':
    main()
