# 최근 풀이 코드

def solution(array):
    temp = []
    numlist = list(set(array))
    array = sorted(array) 
    
    for i in numlist:
        temp.append(array.count(i))
        
    maxnum = max(temp) 
    
    if len(temp) > 1:
        num = temp.count(maxnum)     
        if num >= 2:
            return -1
        else: 
            return numlist[temp.index(maxnum)]
    else: 
        return numlist[temp.index(maxnum)]
        
    
 


# 예전 코드
def solution(array):
    new_array = list(set(array))
    # print('new_array ', new_array)

    cnt = []
    for i in new_array:
        cnt.append(array.count(i))

    # print('cnt       ', cnt)

    reverse_cnt = sorted(cnt, reverse=True)
    # print('reverse_cnt', reverse_cnt)
    # print('max value        ', reverse_cnt[0])
    # print('max         ', cnt.index(reverse_cnt[0]))
    # print('res         ',new_array[cnt.index(reverse_cnt[0])])

    # cnt에서 max 값 가지고 있는 인덱스에 접근. cnt.index(reverse_cnt[0])
    # 접근 후 인덱스 저장 하고 new_array list에 할당 newarray[cnt.index(reverse_cnt[0])]
    if len(cnt) > 1:
        if reverse_cnt[0] == reverse_cnt[1]:
            answer = -1
        else:
            answer = new_array[cnt.index(reverse_cnt[0])]
    else:
        return new_array[0]

    return answer
 
