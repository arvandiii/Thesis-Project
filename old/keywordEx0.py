import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')

# Load your dataset from a CSV file without a header, specify the header name
header_name = 'text'  # Replace with your desired header name
df = pd.read_csv('Filter0/2022-08-23_twitter.csv', usecols=[4], header=None, names=[header_name])

# Extract the text from the specified column
texts = df[header_name].tolist()

# Preprocess the text data
stop_words = set(stopwords.words('english'))

preprocessed_texts = []
for text in texts:
    # Tokenize the text into individual words
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]

    # Add the preprocessed text to the list
    preprocessed_texts.append(filtered_words)

# Combine all the preprocessed texts into a single list
all_words = [word for text in preprocessed_texts for word in text]

# Create a frequency distribution of words
fdist = FreqDist(all_words)

# Select the top keywords based on frequency
num_keywords = 20
top_keywords = [word for word, frequency in fdist.most_common(num_keywords)]

# Print the top keywords
print(f"Top {num_keywords} keywords: {', '.join(top_keywords)}")