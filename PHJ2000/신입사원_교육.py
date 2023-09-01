'''
두 명이 교육되면 둘은 둘의 총합으로 변한다.
모든 신입사원들의 능력치 합을 최소화 시키고 싶다.
능력치 합 만큼 증가한다고 생각하면 편하다.
즉 가장 작은 사람 둘을 계속 부르면 끝
'''
import heapq

def solution(ability, number):
    answer = 0
    hq=[]
    for i in ability:
        heapq.heappush(hq,i)
    for i in range(number):
        s=heapq.heappop(hq)+heapq.heappop(hq)
        heapq.heappush(hq,s)
        heapq.heappush(hq,s)
        
    answer=sum(hq)
    return answer
