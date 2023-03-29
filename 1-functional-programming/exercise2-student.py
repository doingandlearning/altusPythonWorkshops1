from functools import reduce
import string

reviews = [
    {"title": "Film X", "rating": 4.0,
        "review": "A captivating story with great character development."},
    {"title": "Film Y", "rating": 1.5,
        "review": "Disappointing plot and subpar acting."},
    {"title": "Film Z", "rating": 4.5,
        "review": "Incredible cinematography and a powerful performance by the lead actor."},
    {"title": "Film W", "rating": 3.5,
        "review": "A good movie with some memorable moments."},
    {"title": "Film V", "rating": 2.5,
        "review": "An interesting premise, but the execution falls short."},
]


def sentiment_analysis(review):
    text = review.get("review")
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    good_words = ["powerfull", "good", "memorable", "great"]
    bad_words = ["disappointing", "falls", ]
    textarr = text.split(" ")
    sentiment_score = 0
    for word in textarr:
        if word in good_words:
            sentiment_score += 1
        elif word in bad_words:
            sentiment_score -= 1

    if sentiment_score >= 1:
        return "positive"
    elif sentiment_score == 0:
        return "neutral"
    else:
        return "negative"


def add(x, y):
    return x + y['rating']


def add_sentiment(review):
    review['sentiment'] = sentiment_analysis(review)
    return review


avg_rating = reduce(add, reviews, 0)/len(reviews)
print(avg_rating)  # mean


ratings_sentiments = list(map(sentiment_analysis, reviews))
print([add_sentiment(review) for review in reviews])

print(f"ratings_sentiments:{ratings_sentiments}")
