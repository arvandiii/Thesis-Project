import pandas as pd

# Specify the input and output file paths
input_file = "2021-01-01_twitter.csv"
output_file = "tweet.csv"

# Read the input CSV file using pandas
df = pd.read_csv(input_file, nrows=10000)

# Extract the first 20 rows
first_20_rows = df[df.iloc[:, 0] != 'twitter_tweets'].head(10)
print(first_20_rows)

# Save the extracted rows to the output CSV file
first_20_rows.to_csv(output_file, index=False)

print(f"The first 20 rows have been extracted and saved to {output_file}.")