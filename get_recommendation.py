import movie_recommend_by_film as movie
# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title):
    # Get the index of the movie that matches the title
    idx = movie.indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(movie.cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:4]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
#    return movie.df2['title'].iloc[movie_indices]
    x= movie.df2['title'].iloc[movie_indices]
    thefilm='i recommend : ('+') or ('.join(x)
    return (thefilm+')')

