def solution(score):    
    answer = []
    res = []
    
    for i in score:
        temp = sum(i)/2
        answer.append(temp) 
    
    sorted_ans = sorted(answer, reverse=True)
    print(sorted_ans)
    
    for i in answer:
        print(sorted_ans.index(i)+1, end = ' ')
        res.append(sorted_ans.index(i)+1) 
        
    return res