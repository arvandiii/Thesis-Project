import pandas as pd
import emoji
import re
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer

from utils import get_files

normalized_headers = ['type', 'timestamp', 'user', 'text', 'subreddit', 'clean_text']
chunk_size = 10000

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    if not isinstance(text, str): return ""
    text = text.lower()
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = re.sub(r'http\S+|www\S+', ' LINK ', text)
    text = re.sub(r'@\S+', ' MENTION ', text)
    tokens = simple_preprocess(text)
    # tokens = [token for token in tokens if token not in STOPWORDS]
    # tokens = [token for token in tokens if len(token) > 2]
    # tokens = [token for token in tokens if not any(c.isdigit() for c in token)]
    # tokens = [lemmatizer.lemmatize(token) for token in tokens if len(token) > 2]
    cleaned_text = ' '.join(tokens)
    return cleaned_text


def clean(dir_in, dir_out):
    files = get_files(dir_in)
    for file_name, path in files:
        output_path = dir_out + '/' + file_name
        with open(output_path, "w") as f_out:
            for chunk in pd.read_csv(path, header=0, chunksize=chunk_size):
                filtered_chunk = chunk.copy()
                filtered_chunk['clean_text'] = filtered_chunk['text'].apply(clean_text)
                filtered_chunk.to_csv(f_out, header=normalized_headers, index=False, mode="a")