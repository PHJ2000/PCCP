'''
배열 하나를 가지고 추가 한다음 증가시키는 방향으로 진행시키면 될 거같다.
정수기 떄문에 배열도 충분히 가능하다.
아니다. 최대 크기 수가 얼마인지 안나왔으니 딕셔너리로 추가를 하자.
'''
from collections import defaultdict
def solution(array):
    d=defaultdict(str)
    answer = 0
    num=0
    ma=-1
    check=False
    arr=[]
    for i in array: #순회 하면서 딕셔너리에 추가함
        if d[i]=='':
            d[i]=num
            arr.append([i,1])   #키와 0을 저장
            num=num+1   #num을 더해줌
        else:
            arr[d[i]][1]+=1     #값을 증가시킴
            
    for i in range(len(arr)):   #arr의 크기 많큼 돔
        if arr[i][1]>ma:        #값이 ma보다 크다면
            ma=arr[i][1]    #ma를 최신화
            answer=arr[i][0]    #키를 저장함
            check=False     #ch는 거짓으로
        elif arr[i][1]==ma:     #같다면
            answer=-1       #-1로 지정
            check=True      #ch는 참으로
            
    for i in arr:
        print(i)
        
    if check and answer==-1:    #같은 것이 두 개 존재한다면
        return -1       #-1출력
    else:
        return answer
