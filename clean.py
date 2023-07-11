import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string
import re
from textblob import TextBlob
from langdetect import detect

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def clean_text(text):
    # Strip tags using regular expression
    text = re.sub('<.*?>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove multiple white spaces
    text = re.sub('\s+', ' ', text)

    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Remove short words, digits, and stopwords while lowercasing
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    cleaned_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if
                      len(token) > 1 and not token.isdigit() and token.lower() not in stop_words]

    # Remove non-English tokens using the English dictionary
    # english_words = set(wordnet.words())
    # cleaned_tokens = [token for token in cleaned_tokens if token in english_words]

    return " ".join(cleaned_tokens)



def is_text_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False        