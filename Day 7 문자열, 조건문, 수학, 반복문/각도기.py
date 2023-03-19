def solution(angle):
    if angle > 0 and angle < 90:
        return 1
    if angle == 90:
        return 2
    if angle > 90 and angle < 180:
        return 3
    if angle == 180:
        return 4

# 레전드 숏코딩 힙스터 ... 
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer