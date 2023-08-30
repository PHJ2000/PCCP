'''
사진 속 인물의 그리움 점수를 다 모은 것이 사진의 추억점수
그리움 점수가 없을 때, 0으로 친다.
그리워 하는 사람의 이름을 담은 문자열 배열 name
그리움 점수를 담은 정수 배열 yearning
사진들의 추억 점수를 photo
주어진 순서대로 배열에 담아 return하는 함수를 만들어라
'''
from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
   # d=defaultdict(int)
    for i in photo:
        score=0
        for j in i:
            if j in name:
                
                for k in range(len(name)):
                    if name[k]==j:
                        score+=yearning[k]
        answer.append(score)
    return answer
