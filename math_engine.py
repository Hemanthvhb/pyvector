import numpy as np

a=np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
b=np.array([[1,1,1],
            [1,1,1],
            [1,1,1]])
c=a-b
c=c**2
ans=np.sum(c)
print(c)
print(ans)
print(np.sqrt(ans))
