def recommend_movie(movie_ratings, movie_title):
    if movie_title in movie_ratings:
        if movie_ratings[movie_title] >= 8:
            print("You should watch", movie_title)
        else:
            print("You might not enjoy", movie_title, "but here are some recommendations:")

    else:
        print("Movie not found, but here are some recommendations:\n")
        for movie_title in movie_ratings:
            if movie_ratings[movie_title] >= 8:
                print(movie_title, movie_ratings[movie_title])
                print()

movie_ratings = {
    "The Shawshank Redemption": 9.3,
    "The Godfather": 9.2,
    "The Dark Knight": 9.0,
    "Pulp Fiction": 8.9,
    "Schindler's List": 8.9
}

movie_title = input("Enter a movie title: ")

recommend_movie(movie_ratings, movie_title)
