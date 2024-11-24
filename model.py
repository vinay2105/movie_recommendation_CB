import pickle


movie_df = pickle.load(open("movie_df.pkl","rb"))
movie_similarity_df = pickle.load(open("movie_similarity_df.pkl","rb"))

def recommend(movie_name,rating):
    similar_score=movie_similarity_df[movie_name]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    similar_score = list(similar_score.index)
    return similar_score[1:10]



