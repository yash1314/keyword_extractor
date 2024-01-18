import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('stopwords', quiet = True)

class keywords:
  def __init__(self):
    pass

  def word_extractor(self, x):

    words = word_tokenize(x)
    words_list = [i for i in words if i not in string.punctuation]
    words = [word for word in words_list if word not in stopwords.words('english')]

    word_counts = nltk.FreqDist(words)
    final_word_counts = [{i[0]:i[1]}for i in word_counts.most_common(10)]
    return final_word_counts