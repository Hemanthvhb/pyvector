import numpy as np

def euclidean_dist(a,b):
    c=np.array(a)-np.array(b)
    d=np.sum(c**2)
    return np.sqrt(d)
if __name__ == "__main__":
    
    a=[[1,2,3],
        [4,5,6],
        [7,8,9]]
    b=[[1,1,1],
            [1,1,1],
            [1,1,1]]
    print(euclidean_dist(a,b))