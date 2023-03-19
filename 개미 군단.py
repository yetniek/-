def solution(hp): 
    cnt = 0 

    a, hp = divmod(hp, 5) 
    cnt += a
    a, hp = divmod(hp, 3) 
    cnt += a
    a, hp = divmod(hp, 1) 
    cnt += a

    return cnt