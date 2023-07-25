import re
from string import punctuation

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def clean_text(text, lemmatize=False):
    text = re.sub(r'^RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    text = re.sub(r'#', '', text)
    text = ''.join([c for c in text if c not in punctuation])
    text = text.lower()
    text = text.split()

    text = [w for w in text if w not in stop_words]
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    else:
        text = " ".join(text)

    return text
