import os
from pathlib import Path

EXTENSTIONS = ['.csv', '.doc', '.pdf', '.xlsx', '.png', '.jpg', '.jpeg', '.gif', '.webp']
DOC_DIR = "documents/"

def check_extension(file_name):
    ext = Path(file_name).suffix
    return ext in EXTENSTIONS


def check_file_size(file_content, required_size=2):
    file_size = file_content.size / 1024 ** 2
    return file_size <= required_size


def create_file_path(file_name):
    file_path = DOC_DIR + file_name
    return file_path

def save_file(file_path, file_data):
    os.makedirs(os.path.dirname(DOC_DIR), exist_ok=True)
    with open(file_path, 'wb+') as destination:
        for chunk in file_data.chunks():
            destination.write(chunk)
