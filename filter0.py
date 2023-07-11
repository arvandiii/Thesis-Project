import os
import pandas as pd
from clean import clean_text, is_text_english

# Specify the file paths
input_dir = "DB"
output_dir = "Filter0"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the chunk size for processing (adjust as needed)
chunk_size = 10000

keywords0 = ['flood', 'inundation', 'deluge', 'water', 'river', 'creek', 'stream', 'rain', 'storm', 'dam', 'reservoir', 'overflow', 'evacuation', 'rescue', 'damage', 'disaster', 'crisis']

limit = 1
# Twitter
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    output_csv = 'Filter0/' + file_name
    # Check if the file is a compressed tar.gz file
    print(file_name)
    if file_name.endswith("twitter.csv"):
        with open(output_csv, "w") as f_out:
            # Iterate over the chunks of the input CSV file
            for chunk in pd.read_csv(file_path, header=None, chunksize=chunk_size):
                filtered_chunk = chunk[chunk[4].apply(lambda x: any(keyword in str(x).lower() for keyword in keywords0))]

                # Clean the text in the filtered chunk
                filtered_chunk0 = filtered_chunk.copy()
                filtered_chunk0['cleaned_text'] = filtered_chunk[4].apply(clean_text)
                filtered_chunk0['is_en'] = filtered_chunk[4].apply(is_text_english)


                # Write the filtered chunk to the output CSV file
                filtered_chunk0.to_csv(f_out, header=False, index=False, mode="a")
                
        # Print a message indicating the completion
        print("Filtered data saved to", output_csv)
        limit -= 1
    if limit <= 0:
        break


# limit = 3
# # Reddit
# for file_name in os.listdir(input_dir):
#     file_path = os.path.join(input_dir, file_name)
#     output_csv = 'Filter0/' + file_name
#     # Check if the file is a compressed tar.gz file
#     print(file_name)
#     if file_name.endswith("reddit.csv"):
#         with open(output_csv, "w") as f_out:
#             # Iterate over the chunks of the input CSV file
#             for chunk in pd.read_csv(file_path, header=None, chunksize=chunk_size):
#                 # Filter the chunk based on the first attribute
#                 filtered_chunk = chunk[(chunk[0] == "reddit_submissions") & chunk[4].apply(lambda x: any(keyword in str(x).lower() for keyword in keywords0))]
#                 filtered_chunk[4] = filtered_chunk[4].apply(clean_text)

#                 # Write the filtered chunk to the output CSV file
#                 filtered_chunk.to_csv(f_out, header=False, index=False, mode="a")

#         # Print a message indicating the completion
#         print("Filtered data saved to", output_csv)
#         limit -= 0
#     if limit <= 0:
#         break