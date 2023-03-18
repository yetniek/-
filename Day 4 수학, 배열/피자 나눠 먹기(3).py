def solution(slice, n):
    cnt = 0
    
    while(True):
        n = n - slice
        cnt += 1   
        if n <= 0:
            return cnt
            break 
            