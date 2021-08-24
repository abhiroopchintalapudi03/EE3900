import numpy as np

A=np.matrix('8 0; 4 -2; 3 6')
B=np.matrix('2 -2; 4 2; -5 1')
#let C=3X
#2A+3X=5B implies 3X=5B-2A=A*(-2)+B*5
C=np.multiply(A,-2)+np.multiply(B,5)
X=np.multiply(C,1/3)
print(X)