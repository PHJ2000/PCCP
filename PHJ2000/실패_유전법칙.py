'''
Rr : 1 2 1(RR,Rr,rr)
전체 크기는 1,4,16,64
16세대까지 확인함
2
1 2 2 3
1 1 1 1, 1 2 2 3, 1 2 2 3, 3 3 3 3
'''
def solution(queries):
    answer = []
    tree=[] # 1 2 3
    for i in range(16):
        if i==0:
            tree.append([2])
        else:
            di=[]
            for j in range(4**(i-1)):
                if tree[i-1][j]==1:
                    di.append([1])
                    di.append([1])
                    di.append([1])
                    di.append([1])
                elif tree[i-1][j]==2:
                    di.append([1])
                    di.append([2])
                    di.append([2])
                    di.append([3])
                else:
                    di.append([3])
                    di.append([3])
                    di.append([3])
                    di.append([3])
            tree.append(di)
            del di
   
    for i in queries:
        for row,col in i:
            if tree[row][col]==1:
                answer.append("RR")
            elif tree[row][col]==2:
                answer.append("Rr")
            else:
                answer.append("rr")
                 
    return answer

#수식으로 줄일 수 있도록 건드려야 한다
