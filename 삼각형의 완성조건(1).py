def solution(sides):
    num_list = sorted(sides)
    max_len = num_list[-1]
    total = sum(num_list[:-1])
    
    if total > max_len:
        return 1
    else:
        return 2
    