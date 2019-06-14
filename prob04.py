import random

answerset = {dan*su for su in range(1, 10) for dan in range(2, 10)}
l = list(answerset)
while True:
    questset = set()
    dan = random.randrange(2, 10)
    su = random.randrange(1, 10)
    answer = dan * su
    print(dan, ' X ',  su, ' = ?', end='\n\n')
    index = 0
    questset.add(dan * su)
    while True:
        if index == 8:
            break
        num = random.choice(l)
        if num not in questset:
            questset.add(num)
            index += 1

    print(questset.pop(), questset.pop(), questset.pop(), sep='\t')
    print(questset.pop(), questset.pop(), questset.pop(), sep='\t')
    print(questset.pop(), questset.pop(), questset.pop(), sep='\t', end='\n\n')
    num = input('answer : ')
    if num.isdigit():
        num = int(num)
        if answer == num:
            print('정답')
        else:
            print('틀렸습니다.')
        check = input('다시 하시겠습니까? (Y/N) ')
        if check.isalpha() and check.upper() == 'N':
            print('게임을 종료합니다.')
            break
        elif check.isalpha() and check.upper() == 'Y':
            continue
        else:
            print('잘못 입력하셨습니다.')
            break
