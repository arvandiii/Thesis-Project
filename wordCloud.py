import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import string

nltk.download('stopwords')
nltk.download('punkt')


def preprocess_text(text):
    # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    stop_words.update(string.punctuation)
    filtered_words = [word.lower() for word in tokens if word.lower() not in stop_words]

    # Return the preprocessed text as a string
    return ' '.join(filtered_words)


# Load your dataset from a CSV file
df = pd.read_csv('Filter0/2022-08-07_twitter.csv', usecols=[4], header=None, names=['text'])
print(df.head())

# Extract the 'text' column from the dataset
texts = df['text'].tolist()

# Preprocess the text data
preprocessed_texts = [preprocess_text(text) for text in texts]

# Combine all the preprocessed texts into a single string
combined_text = ' '.join(preprocessed_texts)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Visualize the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
