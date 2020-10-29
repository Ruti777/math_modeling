import numpy as np
a = [1, 2, 3]
b = np.array(a)
def mult_func(a):
    c = np.mean(a)
    return(c)
tmp = mult_func(b)
print(tmp)