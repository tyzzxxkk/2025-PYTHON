def gugudan(*dans):
    for dan in dans: #dans에 있는 dan 꺼내기
        for j in range(1, 10): #1부터 9까지 반복
            print(dan, "x", j, "=", dan*j)

gugudan(2, 3, 7)