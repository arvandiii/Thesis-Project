from utils import get_files

def filter_keyword(dir_in, dir_out):
    files = get_files(dir_in)
    for file_name, path in files:
        output_path = dir_out + '/' + file_name
        pass