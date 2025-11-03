class InsufficientBalanceError(Exception):
    pass

class WrongAccountNumberError(Exception):
    pass
# Exception을 상속해서 만든 사용자 정의 예외야.
# 의미:
# InsufficientBalanceError → 잔액이 부족할 때
# WrongAccountNumberError → 계좌 번호가 잘못됐을 때
# pass는 “아무 기능 없고 이름만 있는 예외”라는 뜻.

balance = 1000
amount = -500  # 잘못된 입력 예시
# balance: 현재 계좌 잔액
# amount: 출금하려는 금액 (여기선 -500 → 잘못된 값)
# account: 계좌 정보 (None → 계좌가 존재하지 않음)

if amount <= 0:
    raise ValueError("출금 금액은 0보다 커야 합니다.")
# 출금 금액이 0 이하이면 ValueError 발생
# 메시지: "출금 금액은 0보다 커야 합니다."
# 즉, 음수 출금이나 0원 출금 방지

if not isinstance(amount, (int, float)):
    raise TypeError("금액은 숫자여야 합니다.")
# 출금 금액이 숫자가 아니면 TypeError 발생
# 메시지: "금액은 숫자여야 합니다."
# 문자열이나 다른 타입 방지

if amount > balance:
    raise InsufficientBalanceError("잔액이 부족합니다.")
# 출금 금액이 잔액보다 크면 사용자 정의 예외 발생
# 메시지: "잔액이 부족합니다."

account = None
if account is None:
    raise WrongAccountNumberError("잘못된 계좌 번호입니다.")
# 계좌가 존재하지 않으면 사용자 정의 예외 발생
# 메시지: "잘못된 계좌 번호입니다."