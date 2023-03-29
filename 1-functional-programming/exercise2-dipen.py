from functools import reduce
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

reviews = [
    {"title": "Film X", "rating": 4.0,
        "review": "A captivating story with great character development."},
    {"title": "Film Y", "rating": 1.5,
        "review": "Disappointing plot and subpar acting."},
    {"title": "Film Z", "rating": 4.5, "review": "Incredible cinematography and a powerful performance by the lead"
                                                 " actor."},
    {"title": "Film W", "rating": 3.5,
        "review": "A good movie with some memorable moments."},
    {"title": "Film V", "rating": 2.5,
        "review": "An interesting premise, but the execution falls short."},
]


# Calculate the average rating of all the movies
average_rating = reduce(
    lambda x, y: x + y["rating"], reviews, 0) / len(reviews)
# print(average_rating)

# get the list based on sentiment

# Create an instance of the SentimentIntensityAnalyzer class
analyzer = SentimentIntensityAnalyzer()


def get_movie_by_sentiment(sentiment):
    for review in reviews:
        sentiment_score = analyzer.polarity_scores(review["review"])
        if sentiment_score["compound"] > 0.05:
            review["sentiment"] = "positive"
        elif sentiment_score["compound"] < -0.05:
            review["sentiment"] = "negative"
        else:
            review["sentiment"] = "neutral"

    # Use filter() to find reviews with specified sentiment
    return list(filter(lambda x: x["sentiment"] == sentiment, reviews))


print(get_movie_by_sentiment("positive"))
print(reviews)

# Output: [{'title': 'Film X', 'rating': 4.0, 'review': 'A captivating story with great character development.', 'sentiment': 'positive'}, {'title': 'Film Z', 'rating': 4.5, 'review': 'Incredible cinematography and a powerful performance by the lead actor.',
#                                                                                                                                           'sentiment': 'positive'}, {'title': 'Film W', 'rating': 3.5, 'review': 'A good movie with some memorable moments.', 'sentiment': 'positive'}, {'title': 'Film V', 'rating': 2.5, 'review': 'An interesting premise, but the execution falls short.', 'sentiment': 'positive'}]
