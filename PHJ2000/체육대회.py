'''
[학생 수 ][종목 수]로 구성되어있음
각 종목에 대한 능력치 합이 최대가 되도록
그냥 다 둘려보면 될 것!
'''
from collections import deque
score=0
def solve(ability,start,cnt,vi):    # 전부 탐색한다!
    global score
    score=max(score,cnt)
    students=len(ability)
    sports=len(ability[0])
    if start==sports:
        return
    for student in range(students):
        if vi[student]==0:
            vi[student]=1
            solve(ability,start+1,cnt+ability[student][start],vi)
            vi[student]=0
def solution(ability):
    students=len(ability)
    sports=len(ability[0])
    global score
    vi=[0]*students
    solve(ability,0,0,vi)
    
    answer = 0
    return score

# 불필요한 것은 제거할 필요성이 있다.
