import os
import pandas as pd
from utils import get_files

# files = [fp for fn, fp in get_files('faghatr/filter_lang')]
# print('files', files)

# dfs = [pd.read_csv(f, index_col=0) for f in files]

# # Combine the list of dataframes
# df = pd.concat(dfs, ignore_index=True)


df = pd.read_csv('DB/2022-08-22_reddit.csv', chunksize=100)
print(df.head())

print('Training Set Shape = {}'.format(df.shape))
# print(df["subreddit"].describe())
# counts = df['subreddit'].value_counts().to_dict()
# print(counts)
