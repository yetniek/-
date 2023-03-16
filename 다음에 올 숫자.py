def solution(common):    
    if (common[1] - common[0]) == (common[2] - common[1]): 
        return common[-1]+(common[1] - common[0])
    else:
        if common[1] % common[0] == 0:
            num = common[1]//common[0]  
            print(num)
            return common[-1]*num