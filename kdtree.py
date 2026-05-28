from math_engine import euclidean_dist, cosine_similarity

class KDnode:

    __slots__=['vector','payload','left','right','axis']

    def __init__(self,vector,payload):
        self.vector=vector
        self.payload=payload
        self.left=None
        self.right=None
        self.axis=0

def build(data,depth=0):
    if not data:
        return None

    k=len(data[0][0])
    axis=depth%k 

    data.sort(key=lambda item : item[0][axis])

    mid=len(data)//2

    node=KDnode(data[mid][0],data[mid][1])

    node.axis=axis
    node.left=build(data[:mid],depth+1)
    node.right=build(data[mid+1:],depth+1)

    return node

def search(node,query,best=None):
    if node is None:
        return best

    dist=euclidean_dist(node.vector,query)

    if best is None or dist<best[0]:
        best=(dist,node.payload)

    axis=node.axis
    diff=query[axis]-node.vector[axis]

    close=node.left if diff<=0 else node.right    
    away=node.right if diff<=0 else node.left

    best=search(close,query,best)

    if abs(diff)<best[0]:
        best=search(away,query,best)

    return best

if __name__ == "__main__":
    data = [
        ([1, 2], "cat"),
        ([3, 4], "dog"),
        ([5, 1], "bird"),
        ([9, 8], "fish"),
        ([2, 7], "lion"),
    ]

    root = build(data)
    query = [4, 3]
    result = search(root, query)
    print(f"Closest to {query}: {result[1]} (distance: {result[0]:.3f})")