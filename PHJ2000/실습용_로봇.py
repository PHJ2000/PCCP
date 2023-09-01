'''
R : 오른쪽 회전
L : 왼쪽 회전
G : 한 칸 전진
B : 한 칸 후진
초기에 0,0
'''

def solution(command):
    di=[[1,0],[0,1],[-1,0],[0,-1]]  #북동남서 R
    di_i=0
    answer = []
    r,c=0,0
    for i in command:
        if i=='R':
            di_i=(di_i+1)%4
        elif i=='L':
            di_i=(di_i-1)%4
        elif i=='G':
            r,c=r+di[di_i][0],c+di[di_i][1]
        elif i=='B':
            r,c=r-di[di_i][0],c-di[di_i][1]
        
        
    answer=[c,r]
    return answer
