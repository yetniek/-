#진짜 무식하게 풀었다. 다른 풀이 참고 필수* 

def solution(my_string): 
    num = []
    for i in my_string:
        if i == '1':
            num.append(int(i))
        elif i == '2':
            num.append(int(i))
        elif i == '3':
            num.append(int(i))
        elif i == '4':
            num.append(int(i))
        elif i == '5':
            num.append(int(i))
        elif i == '6':
            num.append(int(i))
        elif i == '7':
            num.append(int(i))
        elif i == '8':
            num.append(int(i))
        elif i == '9':
            num.append(int(i)) 
    return sum(num)