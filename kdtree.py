class KDnode:

    __slots__=['vector','payload','left','right','axis']

    def __init__(self,vector,data):
        self.vector=vector
        self.data=data
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

