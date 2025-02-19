# recommender_model/src/train_svd_model.py
import pandas as pd
from surprise import Dataset, Reader, SVD
import pickle

directory = 'data/movielens/ml-latest-small'

df_movies = pd.read_csv(f'{directory}/movies.csv')
df_ratings = pd.read_csv(f'{directory}/ratings.csv')
df_tags = pd.read_csv(f'{directory}/tags.csv')


df_ratings



# Prepare the data for Surprise library
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df_ratings[['userId', 'movieId', 'rating']], reader)

# Train the SVD model
trainset = data.build_full_trainset()
algo = SVD()
algo.fit(trainset)

# Save the model to a file
with open('models/model_SVD.pkl', 'wb') as f:
    pickle.dump(algo, f)



