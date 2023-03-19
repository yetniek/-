def solution(n, k):
    food = 0
    drink = 0
    
    if n >= 10:
        cnt = n//10  
        food = n * 12000
        drink = (k-cnt)*2000
    else:        
        food = n * 12000
        drink = (k)*2000
         
    return food + drink