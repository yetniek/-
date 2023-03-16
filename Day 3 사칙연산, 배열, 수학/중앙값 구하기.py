def solution(array): 
    array = sorted(array)
    mid_idx = len(array)//2+1  
    answer = array[mid_idx-1]  
    return answer