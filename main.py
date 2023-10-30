from wordlist import worddict
from random import choice
import time


wrong_count: int = 0
wrong = []
correct = []
while len(correct) != 50:
    key = choice([i for i in worddict.keys() if not (i in correct)])
    print(f"{key}: ", end='')
    word = input()
    if word == worddict[key]:
        print("정답!")
        correct.append(key)
    else:
        wrong_count += 1
        if not(key in wrong):
            wrong.append(key)
        print(f'오답, 정답은: {worddict[key]}')
        time.sleep(2)

print(f'종료, 틀린 횟수: {wrong_count}')
if wrong_count > 0:
    print(f'한번 이상 틀린 단어: ')
for key in wrong:
    print(f'    {key}: {worddict[key]}')
