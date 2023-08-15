import os
import pandas as pd
from clean import clean_text, is_text_english

input_dir = "Filter0"
output_dir = "Filter_lang"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

chunk_size = 10000

limit = 1000
# Twitter
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    output_csv = output_dir + '/' + file_name
    print(file_name)
    if file_name.endswith("twitter.csv"):
        with open(output_csv, "w") as f_out:
            for chunk in pd.read_csv(file_path, header=None, chunksize=chunk_size):
                filtered_chunk = chunk[chunk[8].apply(is_text_english)]
                filtered_chunk.to_csv(f_out, header=False, index=False, mode="a")
        print("Filtered data saved to", output_csv)
        limit -= 1
    if limit <= 0:
        break


limit = 1000
# Reddit
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    output_csv = output_dir + '/' + file_name
    print(file_name)
    if file_name.endswith("reddit.csv"):
        with open(output_csv, "w") as f_out:
            for chunk in pd.read_csv(file_path, header=None, chunksize=chunk_size):
                filtered_chunk = chunk[chunk[8].apply(is_text_english)]
                filtered_chunk.to_csv(f_out, header=False, index=False, mode="a")

        print("Filtered data saved to", output_csv)
        limit -= 0
    if limit <= 0:
        break