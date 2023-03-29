import string
from collections import Counter
from operator import itemgetter


def top_n_words(text, n):
    # Clean the text by making it lowercase and removing punctuation
    cleaned_text = text.lower().translate(str.maketrans("", "", string.punctuation))

    # Split the cleaned text into a list of words
    words = cleaned_text.split()

    # Count the frequency of each word using the Counter class from the collections module
    word_frequencies = Counter(words)

    # Sort the word frequencies in descending order using the sorted function and itemgetter
    sorted_word_frequencies = sorted(
        word_frequencies.items(), key=itemgetter(1), reverse=True)

    # Return the top N words by frequency
    return sorted_word_frequencies[:n]


text = "Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions or declarations instead of statements."
top_n = 5

# Expected output: [('programming', 4), ('and', 2), ('is', 3), ('a', 2), ('paradigm', 2)]
print(top_n_words(text, top_n))
