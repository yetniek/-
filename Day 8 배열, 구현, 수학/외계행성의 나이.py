def solution(age):
    answer = '' 
    chars = [chr(i) for i in range(97, 107)]
    temp = str(age)
    for i in temp:    
        answer += chars[int(i)]
    return answer