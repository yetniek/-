def solution(emergency):
    emer = sorted(emergency, reverse = True)  
    return [emer.index(i)+1 for i in emergency]