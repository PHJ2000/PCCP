'''
k초마다 카페에 줄 섬
주문 받은 대로 음료 제가(1개씩) - 받으면 나감
주문받은 음료 목록으로 동시에 몇 명 있었는지 알고 싶음
음료 0~
'''
def solution(menu, order, k):
    answer = 0
    ma=0
    su=0
    vi=[0]*len(order)
    ti=[0]*len(order)
    for i in range(len(order)):
        vi[i]=1
        ti[i]=menu[order[i]]
        su=sum(vi)
        for j in range(i):
            if vi[j]==1:    #주문중에 있다면
                ti[j]-=k
                if ti[j]<=0:
                    ti[j]=0
                    vi[j]=0
        answer=max(answer,su)
        
    return answer


#음료를 시키면 앞에 음료수가 다 끝나야지 제작이 가능하다는 것을 관과했다. 큐를 써야하네
