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

def search(node, query, best=None):
    if node is None:
        return best

    dist = euclidean_dist(node.vector, query)

    if best is None or dist < best[0]:
        best = (dist, node.payload)

    axis = node.axis
    diff = query[axis] - node.vector[axis]

    if diff <= 0:
        best = search(node.left, query, best)
    else:
        best = search(node.right, query, best)

    if abs(diff) < best[0]:
        if diff <= 0:
            best = search(node.right, query, best)
        else:
            best = search(node.left, query, best)

    return best

def insert(node,vector,payload,depth=0):
    if node is None:
        return KDnode(vector,payload)

    axis = depth % len(vector)
    if vector[axis]<node.vector[axis]:
        node.left= insert(node.left,vector,payload,depth+1)
    else:
        node.right= insert(node.right,vector,payload,depth+1)

    return node

if __name__ == "__main__":
    data = [
        ([1, 2], "cat"),
        ([3, 4], "dog"),
        ([5, 1], "bird"),
        ([9, 8], "fish"),
        ([2, 7], "lion"),
    ]

    root = build(data)
    
    root = insert(root, [6, 5], "tiger")
    result2 = search(root, [6, 4])
    print(f"Closest to [6,4]: {result2[1]} (distance: {result2[0]:.3f})")
