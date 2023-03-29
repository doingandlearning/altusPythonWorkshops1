import string
from collections import Counter


def top_n_words_yoseph(text, top_n):
    words = [word.lower().translate(str.maketrans("", "", string.punctuation))
             for word in text.split(" ")]
    return list(dict(Counter(words)).items())[:top_n]


def top_n_words_dipen(input_text, n):
    # Remove punctuation and convert text to lowercase
    input_text = input_text.translate(
        str.maketrans('', '', string.punctuation)).lower()

    words = input_text.split(" ")
    return Counter(words).most_common(n)


text = "Functional programming is a programming paradigm that treats computation as the evaluation of mathematical " \
       "functions and avoids changing state and mutable data. It is a declarative programming paradigm, which means " \
       "programming is done with expressions or declarations instead of statements."
top_n = 5

print(top_n_words(text, top_n))
