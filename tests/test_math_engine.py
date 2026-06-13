from math_engine import euclidean_dist, cosine_similarity

def test_euclidean_known_distance():
    result = euclidean_dist([0, 0], [3, 4])
    assert round(result, 5) == 5.0

def test_cosine_orthogonal_vectors():
    result = cosine_similarity([1, 0], [0, 1])
    assert round(result, 5) == 0.0