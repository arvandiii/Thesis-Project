import pandas as pd
import emoji
import re
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer
import fasttext

from utils import get_files

normalized_headers = ['type', 'timestamp', 'user', 'text', 'subreddit', 'clean_text']
chunk_size = 10000

def clean_text(text):
    if not isinstance(text, str): return ""
    text = text.lower()
    text = emoji.replace_emoji(text, "")
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    tokens = simple_preprocess(text)
    cleaned_text = ' '.join(tokens)
    return cleaned_text

model = fasttext.load_model('lid.176.bin')

def is_eng(text):
    text = clean_text(text)
    prediction = model.predict(text)
    print(prediction[0], text)
    return prediction[0][0] == '__label__en'


def filter_relevant(dir_in, dir_out):
    files = get_files(dir_in)
    for file_name, path in files:
        output_path = dir_out + '/' + file_name
        with open(output_path, "w") as f_out:
            for chunk in pd.read_csv(path, header=0, chunksize=chunk_size):
                filtered_chunk = chunk[chunk['text'].apply(is_eng)]
                filtered_chunk.to_csv(f_out, header=normalized_headers, index=False, mode="a")
        

#Active learning
#BERT
#Clustring