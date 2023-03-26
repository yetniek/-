def solution(rsp):
    r, s, p = '0', '2', '5'
    answer = ''
    
    for i in rsp:
        if i == r:
            answer += '5'
        if i == s:
            answer += '0'
        if i == p:
            answer += '2'
    return answer