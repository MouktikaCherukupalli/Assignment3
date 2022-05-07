import numpy as np
from numpy import linalg as LA
from numpy import random aS RN
N=100

#generating random variables
X = RN.randint(0,high=10,size=N}
Count1=np.count_nonzero(X<=6)
Count2=N-Count1
print(Count2/N}

#theoritical probabilities
pr_1=0.62
pr_2=1-pr_1
print(pr_2)