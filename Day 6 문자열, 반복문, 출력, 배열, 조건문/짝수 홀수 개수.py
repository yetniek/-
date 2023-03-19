def solution(num_list):
    cnt_even = 0 #짝
    cnt_odd = 0 #홀
    
    for i in num_list:
        if i%2 == 0:
            cnt_even += 1
        else:
            cnt_odd +=1
            
    answer = [cnt_even, cnt_odd]
    return answer