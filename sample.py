import os
import pandas as pd

input_dir = "DB"
output_dir = "sampleDB"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

chunk_size = 10000

limit = 10
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    output_csv = output_dir + '/' + file_name
    print(file_name)
    if file_name.endswith("_reddit.csv"):
        with open(output_csv, "w") as f_out:
            for chunk in pd.read_csv(file_path, header=None, chunksize=chunk_size):
                chunk.to_csv(f_out, header=False, index=False, mode="a")
        print("Filtered data saved to", output_csv)
        limit -= 1
    if limit <= 0:
        break