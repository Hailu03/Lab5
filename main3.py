# Sample dataset for movie recommendations
dataset = {
    'movie1': {'action': 1, 'thriller': 1, 'comedy': 0, 'romance': 0,'adventure':0},
    'movie2': {'action': 0, 'thriller': 0, 'comedy': 1, 'romance': 1,'adventure':0},
    'movie3': {'action': 1, 'thriller': 0, 'comedy': 0, 'romance': 0,'adventure':1},
    'movie4': {'action': 0, 'thriller': 0, 'comedy': 1, 'romance': 0,'adventure':0},
    'movie5': {'action': 0, 'thriller': 1, 'comedy': 0, 'romance': 0,'adventure':1},
    'movie6': {'action': 1, 'thriller': 0, 'comedy': 1, 'romance': 0,'adventure':0},
    'movie7': {'action': 0, 'thriller': 0, 'comedy': 0, 'romance': 1,'adventure':0},
    'movie8': {'action': 0, 'thriller': 1, 'comedy': 0, 'romance': 0,'adventure':0},
    'movie9': {'action': 1, 'thriller': 0, 'comedy': 0, 'romance': 0,'adventure':0},
    'movie10': {'action': 0, 'thriller': 0, 'comedy': 1, 'romance': 1,'adventure':0}
}

def content_based_recommender(dataset, user_preferences, num_recommendations=5):
    # Compute weighted sums
    scores = {}
    for movie in dataset:
        features = dataset[movie]
        weighted_sum = sum(features[genre] for genre in user_preferences)
        scores[movie] = weighted_sum

    # Sort the scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Generate recommendations
    recommendations = []
    for movie, score in sorted_scores:
        if movie not in user_preferences:
            recommendations.append(movie)
        if len(recommendations) == num_recommendations:
            break

    return recommendations

# Example usage
user_preferences = ['action', 'adventure']
recommendations = content_based_recommender(dataset, user_preferences)
print("Recommendations:", recommendations)
