import re
import nltk

from nltk.corpus import stopwords

# Download stopwords once
try:
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

stop_words = set(stopwords.words('english'))

def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Remove stopwords
    words = text.split()

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    cleaned_text = " ".join(filtered_words)

    return cleaned_text