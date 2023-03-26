def fact(num): 
    f = 1
    for i in range(1, num+1): 
        f = f*i 
    return f

def solution(balls, share):
    a = fact(balls) 
    b = fact(balls-share)
    c = fact(share)
    print(a, b, c) 
    print(a//(b*c)) 
    return a//(b*c)