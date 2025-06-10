import random

def dice_list(pip=6, repeat=1): #pip=주사위 면의 수, repeat=주사위 굴리는 횟수
    result = [] #값을 저장하는 리스트
    for r in range(1, repeat+1): #1부터 repeat까지 반복
        n = random.randint(1, pip) #1부터 pip까지의 정수를 하나 뽑음
        result.append(n) #결과 리스트에 추가
    return result

print(dice_list(6, 3))