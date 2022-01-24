"""
TODO

1. Sort user movies by top rated
2. Get top 10 movies by user
"""

import pandas as pd
from surprise import dump
import utils

MOVIES_FILE = 'ml-100k/u.item'
RATINGS_FILE = 'ml-100k/u.data'

# Ask input for user ID
while True:
    try:
        user_id = int(input("Enter user ID (1-943): "))
    except:
        continue
    else:
        if user_id >= 1 and user_id <= 943:
            break
        else:
            continue

# Ask for the number of recommendations
while True:
    try:
        n_recs = int(input("Enter number of recommendations (1-10): "))
    except:
        continue
    else:
        if n_recs >= 1 and n_recs <= 10:
            break
        else:
            continue
print()

# Load the datasets
movies = pd.read_table(
    MOVIES_FILE,
    names=['id', 'title'],
    sep='|',
    encoding='cp1252',
    usecols=[0, 1]
)
ratings = pd.read_table(
    RATINGS_FILE,
    names=['user_id', 'movie_id', 'rating'],
    sep='\t',
    encoding='cp1252',
    usecols=[0, 1, 2]
)

# Show movies the user has rated
movies_rated = ratings['movie_id'][ratings['user_id'] == user_id]
movies_rated = movies['title'][movies['id'].isin(movies_rated)].tolist()

print(f"User #{user_id} rated these movies:")
for movie in movies_rated:
    print(" ", movie)
print()

# Load predictions and show recommendations
predictions, _ = dump.load('algorithms/svdpp')
top_n = utils.get_top_n(predictions, n=n_recs)
top_n = [int(item_id) for (item_id, _) in top_n[str(user_id)]]

recommendations = movies['title'][movies['id'].isin(top_n)].tolist()

print(f"Recommended movies to user #{user_id}:")
for movie in recommendations:
    print(" ", movie)
