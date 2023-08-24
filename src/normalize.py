import pandas as pd
from utils import get_files


# normalized_headers = ['type', 'timestamp', 'user', 'text', 'subreddit', 'comments', 'retweets', 'likes']
normalized_headers = ['type', 'timestamp', 'user', 'text', 'subreddit']

chunk_size = 10000

def normalize_twitter(path, output_path):
    return
    columns_to_save = [0,2,3,4]
    with open(output_path, "w") as f_out:
        for chunk in pd.read_csv(path, header=None, chunksize=chunk_size):
            filtered_chunk = chunk.iloc[:, columns_to_save].copy()
            filtered_chunk['subreddit'] = 'NA'
            filtered_chunk.to_csv(f_out, header=normalized_headers, index=False, mode="a")
    

def normalize_reddit(path, output_path):
    columns_to_save = [0,2,3,4,7]
    with open(output_path, "w") as f_out:
        for chunk in pd.read_csv(path, header=None, chunksize=chunk_size):
            filtered_chunk = chunk.iloc[:, columns_to_save].copy()
            filtered_chunk = filtered_chunk[filtered_chunk[0] == 'reddit_submissions']
            filtered_chunk.to_csv(f_out, header=normalized_headers, index=False, mode="a")

def normalize(dir_in, dir_out):
    files = get_files(dir_in)
    for file_name, path in files:
        output_path = dir_out + '/' + file_name
        if file_name.endswith('twitter.csv'):
            normalize_twitter(path, output_path)
        elif file_name.endswith('reddit.csv'):
            normalize_reddit(path, output_path)