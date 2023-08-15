from utils import get_files

def clean_twitter():
    pass

def clean_reddit():
    pass

def clean(dir_in, dir_out):
    files = get_files(dir_in)
    for file_name, path in files:
        output_path = dir_out + '/' + file_name
        if file_name.endswith('twitter.csv'):
            clean_twitter(path, output_path)
        elif file_name.endswith('reddit.csv'):
            clean_reddit(path, output_path)
    