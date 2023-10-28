from wordlist import worddict
from random import choice


correct = []
while len(correct) != 50:
    key = choice(list(worddict.keys()))
    while key in correct:
        key = choice(list(worddict.keys()))
    print(f"{key}: ", end='')
    word = input()
    if word == worddict[key]:
        print("정답!")
        correct.append(key)
    else:
        print(f'오답, 정답은: {worddict[key]}')


print('종료')