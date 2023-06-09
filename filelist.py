import os
import concurrent.futures
from pathlib import Path
import time
import math

class Counters:
    def __init__(self):
        self.files = 0
        self.directories = 0
        self.inaccessible = 0
        self.file_extensions = {}
        self.largest_file = {"name": "", "size": 0}
        self.total_size = 0

def list_files(path, counters=None):
    try:
        for item in os.scandir(path):
            if item.is_file():
                print(f'{item.path}')
                counters.files += 1
                file_extension = os.path.splitext(item.name)[1]
                counters.file_extensions[file_extension] = counters.file_extensions.get(file_extension, 0) + 1
                file_size = item.stat().st_size
                counters.total_size += file_size
                if file_size > counters.largest_file["size"]:
                    counters.largest_file["name"] = item.name
                    counters.largest_file["size"] = file_size
            elif item.is_dir():
                print(f'{item.path}')
                counters.directories += 1
                list_files(item.path, counters)
    except PermissionError:
        print(f'Permission denied: {Path(path).resolve()}')
        counters.inaccessible += 1

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    size = round(size_bytes / math.pow(1024, i), 2)
    return f"{size} {size_names[i]}"

def traverse_directory(root_directory, counters):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(list_files, root_directory, counters)

def main():
    root_directory = input("Enter the root directory path: ")
    root_directory = root_directory.strip()

    if not os.path.isdir(root_directory):
        print(f'Error: "{root_directory}" is not a valid directory.')
        return

    print(f'Listing all files and directories in: {Path(root_directory).resolve()}\n')
    counters = Counters()

    start_time = time.time()

    traverse_directory(root_directory, counters)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nSummary:")
    print(f"Files: {counters.files}")
    print(f"Directories: {counters.directories}")
    print(f"Inaccessible: {counters.inaccessible}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print("\nAdditional Statistics:")
    print("File Extensions (sorted by occurrence count):")
    sorted_extensions = sorted(counters.file_extensions.items(), key=lambda x: x[1], reverse=True)
    for extension, count in sorted_extensions:
        print(f"{extension}: {count}")
    print(f"Largest File: {counters.largest_file['name']} ({convert_size(counters.largest_file['size'])})")
    print(f"Total Size: {convert_size(counters.total_size)}")

if __name__ == '__main__':
    main()
