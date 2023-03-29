from functools import reduce

reviews = [
    {"title": "Movie A", "rating": 3.5,
        "review": "It was an average movie with decent acting."},
    {"title": "Movie B", "rating": 4.5,
        "review": "An amazing experience! Loved the visual effects."},
    {"title": "Movie C", "rating": 2.0, "review": "Poor acting and a weak storyline."},
    {"title": "Movie D", "rating": 3.0,
        "review": "An okay movie. Could have been better."},
    {"title": "Movie E", "rating": 5.0,
        "review": "A true masterpiece! I highly recommend it."},
]

# map
# [].map()


def extract_title(review):
    return review['title']


titles_with_builtin = list(map(extract_title, reviews))
print(reviews)
print(titles_with_builtin)

titles_with_comp = [extract_title(review) for review in reviews]

print(titles_with_comp)


# filter
def good_movie(review):
    return review['rating'] >= 3.5


good_reviews_filter = list(filter(good_movie, reviews))

print(good_reviews_filter)

good_reviews_comp = [review for review in reviews if good_movie(review)]

print(good_reviews_comp)

# reduce


def add(x, y):
    return x + y['rating']


total_rating = reduce(add, reviews, 0)
print(total_rating)
