'''
같은 키를 여러분 누르면 변경됨
특정 문자열을 작성할 때, 키를 최소 몇 번 눌려야 하는지
문자열 배열 keymap
입력하려는 물자열들이 담긴 문자열 배열 targets
keymap에서 최소값을 찾아내내서 덧셈을 성공시켜야 한다.
'''
from collections import defaultdict
def solution(keymap, targets):
    answer = []
    for target in targets:
        su=0
        for tstr in target: #타겟의 문자열
            mi=500
            for key in keymap: #하나의 키
                if tstr in key: #타겟 문자가 키에 있는가
                    for kidx in range(len(key)): #몇번째의 해당하는가
                        if key[kidx]==tstr: #키문자열와 타겟 문자가 일치하는가
                            if mi>kidx+1:
                                mi=kidx+1
                                break
            if mi!=500:
                su+=mi
            else:
                su=-1
                break
        answer.append(su)
    return answer

#defaultdict을 활용해서 풀어볼 것!
