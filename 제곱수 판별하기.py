import numpy as np
def solution(n):  
    if str(np.sqrt(n)).split(".")[1]  == '0':
        return 1
    else:
        return 2
    