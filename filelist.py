import os
from pathlib import Path

def list_files(path, indentation=''):
    try:
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                print(f'{indentation}|- {item}')
            elif os.path.isdir(item_path):
                print(f'{indentation}|+ {item}')
                list_files(item_path, indentation + '|  ')
    except PermissionError:
        print(f'{indentation}|! Permission denied: {Path(path).resolve()}')

def main():
    root_directory = input("Enter the root directory path: ")
    root_directory = root_directory.strip()

    if not os.path.isdir(root_directory):
        print(f'Error: "{root_directory}" is not a valid directory.')
        return

    print(f'Listing all files and directories in: {Path(root_directory).resolve()}\n')
    list_files(root_directory)

if __name__ == '__main__':
    main()
