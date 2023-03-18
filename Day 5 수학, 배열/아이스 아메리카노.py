def solution(money):
    answer = []
    
    coffee = int(money//5500)
    money = int(money%5500)
    
    answer = [coffee, money]
    return answer