'''
bfs구조로 만들게 되면 된다.
큐 형식으로 집어넣게

'''
    
def solution(maps):
    answer = 0
    i,j=0,0
    di=[[0,1],[1,0],[0,-1],[-1,0]]
    qu=[]
    n=len(maps)
    m=len(maps[0])
    maps[n-1][m-1]=2000
    cnt=0
    vi=[]
    for _ in range(n):
        vi.append([0]*m)
    qu.append([0,0,1])
    while len(qu)!=0:
        i,j,cnt=qu.pop()
        maps[i][j]=cnt
        vi[i][j]=-1
        for v in range(4):
            dz,do=di[v]
            if i+dz<0 or i+dz>=n or j+do<0 or j+do>=m or maps[i+dz][j+do]!=1 or vi[i+dz][j+do]==-1:
                continue
            if vi[i+dz][j+do]==-1:
                qu.append([i+dz,j+do,min(maps[i+dz][j+do],maps[i][j]+1)])
                maps[i+dz][j+do]=min(maps[i+dz][j+do],maps[i][j]+1)
                vi[i+dz][j+do]=-1
            else:
                qu.append([i+dz,j+do,maps[i][j]+1])
                maps[i+dz][j+do]=maps[i][j]+1
                vi[i+dz][j+do]=-1
    for i in range(n):
        for j in range(m):
            print(maps[i][j],end=" ")
        print()
    
    return 0
    if maps[n-1][m-1]==2000:
        return -1
    else:
        return maps[n-1][m-1]
