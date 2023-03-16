# numer : 분자
# denom : 분모

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b / GCD(a, b)

def solution(numer1, denom1, numer2, denom2):
    lcm = LCM(denom1, denom2)   
    
    if denom1 == lcm:
        new_n1 = numer1
        new_n2 = numer2
        
    if denom2 == lcm:
        new_n1 = numer1
        new_n2 = numer2
        
    if denom1 != lcm:  
        temp1 = lcm//denom1  
        new_d1 = denom1 * temp1 
        new_n1 = numer1 * temp1  
        
    if denom2 != lcm:  
        temp2 = lcm//denom2  
        new_d2 = denom2 * temp2
        new_n2 = numer2 * temp2 
         
    n_res = int(new_n1 + new_n2)
    d_res = int(lcm)
    
    cnt = GCD(n_res, d_res)
    res = [n_res//cnt, d_res//cnt]
    return res