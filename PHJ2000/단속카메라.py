'''
모든 차량이 단속용 카메라를 한 번은 만나도록 설치하고 함
겹치는 경우가 많은 것을 보고 겹치는 부분을 보자
routes[i][0] 들어온 지점 routes[i][1] 나간 지점
최소 몇 대의 카메라를 설치해야 하는가?

경우의 수
a b c d라고 할 때
a>c and b>d
'''
def solution(routes):
    answer = 1
    
    routes.sort(key=lambda r: r[1])
    
    #print(routes)
    
    point=routes[0][1] # -15
    
    for r in routes[1:]:
        # -15
        if r[0] > point:
            point = r[1]
            answer += 1
    
    return answer
