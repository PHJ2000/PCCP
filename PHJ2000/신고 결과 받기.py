'''
유저당 한 번에 한 명 신고가능
신고 횟수 제한 없음
동일한 유저에 대한 신고는 1회로 처리
k번 이상 신고된 유저는 게시판 이용 정지, 해당 유저를 신고한 모든 유저에게 메일 전송
처리 결과 메일을 받은 횟수를 반환
이용자id 신고한 id
자기자신을 신고하진 않음
'''
from collections import defaultdict
def solution(id_list, report, k):
    d = defaultdict(list)
    
    id_li = defaultdict(int)
    answer = [0]*len(id_list)
    
    for i_idx, i in enumerate(id_list):  # id와 순서를 매김
        id_li[i]=i_idx
        
    
    for rstr in set(report):
        a, b=rstr.split() #분리 시킴 [0] 이용자 [1] 신고대상
        d[b].append(a)
    
    for b_u, v in d.items(): #신고한 대상 딕셔너리
        
        if len(v) >= k: #넘으면
            for u in v:  #신고한 대상을 순회
                answer[ id_li[ u ] ] += 1
            
    return answer
