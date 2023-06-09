import os

def list_files(path, indentation=''):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print(f'{indentation}- {item}')
        elif os.path.isdir(item_path):
            print(f'{indentation}+ {item}')
            list_files(item_path, indentation + '  ')

# Provide the root directory path here
root_directory = './'

list_files(root_directory)
