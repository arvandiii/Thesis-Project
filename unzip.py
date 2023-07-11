import os
import tarfile

# Specify the input directory containing the tar.gz files
input_dir = "compresedDB"

# Specify the output directory for extracted files
output_dir = "DB"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over the files in the input directory
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)

    # Check if the file is a compressed tar.gz file
    if file_name.endswith(".tar.gz"):
        # Extract the file into the output directory
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(output_dir)

        print(f"Extracted {file_name} into {output_dir}.")