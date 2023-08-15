import os

def get_files(input_dir):
    return [(file_name, os.path.join(input_dir, file_name)) for file_name in os.listdir(input_dir)]

