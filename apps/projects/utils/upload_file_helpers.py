import os
from pathlib import Path

EXTENSTIONS = ['.csv', '.doc', '.pdf', '.xlsx']

def check_extension(file_name):
    ext = Path(file_name).suffix
    return ext in EXTENSTIONS


def check_file_size(file, required_size=2):
    file_size = file.size / (1024 * 1024)
    return file_size <= required_size


def create_file_path(file_name):
    file_path = "documents/" + file_name
    return file_path

def save_file(file_path, file_data):
    os.makedirs(os.path.dirname('documents/'), exist_ok=True)
    with open(file_path, 'wb+') as destination:
        for chunk in file_data.chunks():
            destination.write(chunk)
