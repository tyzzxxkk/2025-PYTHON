score = int(input("점수를 입력하세요: "))

if score >= 70:
    if score >= 80:
        if score >= 90:
            print("A")
        else:
            print("B")
    else:
        print("C")
else:
    print("F") 
