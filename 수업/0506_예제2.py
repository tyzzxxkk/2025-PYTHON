text = "ABCDEFGHIJ" #주어진 문자열

even_chars = [] #짝수 인덱스의 문자를 저장할 리스트

for i in range(len(text)) : #문자열 길이만큼 반복
    if i % 2 == 0 : #인덱스가 짝수인지 확인
        even_chars.append(text[i]) #짝수 인덱스의 문자 추가

for i in range(len(even_chars)- 1, -1, -1) : #리스트의 마지막 인덱스부터 0까지 거꾸로 반복
    print(even_chars[i], end="") #줄바꿈 없이 문자 출력