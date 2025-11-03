email = []

n = int(input("개수를 입력하세요: "))

for i in range(n):
    mail = input(f"{i+1}번째 이메일을 입력하세요: ")

    if '@' in mail and '.' in mail:
        at = mail.find('@')
        dot = mail.rfind('.')
        if at > 0 and dot > at:
            domain = mail[at+1:]
            if domain.count('.') == 1:
                email.append(mail)

print("\n올바른 이메일 목록:")
for e in email:
    print(e)