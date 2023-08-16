import pandas as pd
from utils import get_files

normalized_headers = ['type', 'timestamp', 'user', 'text', 'subreddit']
chunk_size = 10000

keywords0 = ['flood', 'inundation', 'deluge', 'water', 'river', 'creek', 'stream', 'rain', 'storm', 'dam', 'reservoir', 'overflow', 'evacuation', 'rescue', 'damage', 'disaster', 'crisis']

def filter_keyword(dir_in, dir_out):
    files = get_files(dir_in)
    for file_name, path in files:
        output_path = dir_out + '/' + file_name
        with open(output_path, "w") as f_out:
            for chunk in pd.read_csv(path, header=0, chunksize=chunk_size):
                filtered_chunk = chunk[chunk['text'].apply(lambda x: any(keyword in str(x).lower() for keyword in keywords0))]
                filtered_chunk.to_csv(f_out, header=normalized_headers, index=False, mode="a")
        