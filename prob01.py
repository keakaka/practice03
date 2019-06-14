# 다음 세 개의 리스트가 있을 때,
# 3형식 문장을 모두 출력해 보세요. 반드시 comprehension을 사용합니다.

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

for s in subs:
    for s2 in verbs:
        for s3 in objs:
            print(s, s2, s3)