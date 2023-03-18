def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(n):
    #6조각으로 나눔
    #n과 조각의 최소공배수 
    num = lcm(6, n)
    res = num//6 
    return res
            