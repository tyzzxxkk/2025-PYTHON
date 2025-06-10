now = int(input("현재 몸무게를 입력하세요 : "))
goal = int(input("목표 몸무게를 입력하세요 : "))

week = 1

while now > goal :
    lose = int(input(f"{week}주차 감량 몸무게 : "))
    now -= lose
    week += 1

print(f"{goal}kg 달성! 축하합니다!")