def game():
    print("2의 제곱 숫자 맞추기 게임을 시작합니다!")
    print("게임을 중간에 종료하려면 'end'를 입력하세요.\n")

    chance = 50  # 기회는 총 50번
    current = 0  # 2^0부터 시작

    while chance > 0:
        answer = 2 ** current  # 맞추어야 할 2의 제곱 값

        # 사용자 입력 받기
        num = input(f"{current + 1}번째 문제 - 2의 제곱을 입력하세요: ")

        if num.lower() == "end":  # 중간에 종료
            print("게임을 종료합니다.")
            break

        if num.isdigit():  # 숫자인지 확인
            if int(num) == answer:  # 정답을 맞춘 경우
                print("정답!")
                current += 1  # 정답을 맞추면 다음 제곱으로 넘어감
            else:  # 틀린 경우
                print("다시 입력하세요.")
        else:  # 숫자가 아닌 입력에 대해서
            print("숫자 또는 'end'를 입력해주세요.")

        chance -= 1  # 기회 차감

    if chance == 0:  # 기회 소진 시 종료 메시지 출력
        print("기회가 모두 소진되었습니다. 게임을 종료합니다.")

# 게임 시작
game()
