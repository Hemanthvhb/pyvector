import numpy as np

def euclidean_dist(a,b):
    c=np.array(a)-np.array(b)
    d=np.sum(c**2)
    return np.sqrt(d)

def cosine_similarity(a,b):
    na=np.array(a)
    nb=np.array(b)
    return np.dot(na,nb)/((np.linalg.norm(na))*(np.linalg.norm(nb)))

def batch_euclidean(query, matrix):
    matrix = np.array(matrix)
    query = np.array(query)
    return np.sqrt(np.sum((matrix - query) ** 2, axis=1))   

def batch_cosine_similarity(query, matrix):
    matrix = np.array(matrix)
    query = np.array(query)
    return (matrix @ query)/((np.linalg.norm(matrix,axis=1))*(np.linalg.norm(query)))  

if __name__ == "__main__":
    
    a=[1,2,3]
    b=[1,1,1]
    print(euclidean_dist(a,b))
    print(cosine_similarity(a,b))
    query = [1, 2, 3]
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    print(batch_euclidean(query, matrix))
    print(batch_cosine_similarity(query,matrix))