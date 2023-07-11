import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from gensim import corpora, models
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

# Create a dictionary and corpus
dictionary = corpora.Dictionary(preprocessed_texts)
corpus = [dictionary.doc2bow(text) for text in preprocessed_texts]

# Perform LDA topic modeling
num_topics = 5  # Number of topics to generate
lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

# Extract and print the most used keywords for each topic
for topic_id in range(num_topics):
    topic_keywords = lda_model.show_topic(topic_id, topn=10)
    keyword_list = [keyword for keyword, _ in topic_keywords]
    print(f"Topic {topic_id + 1}: {', '.join(keyword_list)}")
