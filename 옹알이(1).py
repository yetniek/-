# 조합, 순열 주의. 
# test cast 8 error : ["ayaye", "ayaye", "uuuma", "ye", "yemawoo", "ayaa"] : 4  
# 마지막 check / res 부분 수정

from itertools import permutations

def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    list_2 = list(permutations(word,2)) 
    list_3 = list(permutations(word,3)) 
    list_4 = list(permutations(word,4)) 
    lst = list_2 + list_3 + list_4 
    
    temp = [] 
    check = []
    
    for i in lst:
        i = list(i)
        temp.append(i)
        
    for words in temp:  
        str = ''
        for i in words: 
            str += i
            check.append(str) 
            
    check += word 
    check = list(set(check)) 
    
    for i in check: 
        for j in babbling:
            if j == i:
                answer += 1
    
    return answer