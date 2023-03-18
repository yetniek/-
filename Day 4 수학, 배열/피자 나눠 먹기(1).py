def solution(n):
    cnt = 0
    
    while(True): 
        n = n-7 
        cnt += 1
        
        if n <= 0:
            return cnt
            break
            
        