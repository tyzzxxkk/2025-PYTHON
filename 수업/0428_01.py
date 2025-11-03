list = [1, 2, 3, 4, 5, 6 ,7] #주어진 리스트

value = int(input("삭제할 값을 입력 : ")) #삭제할 값을 입력받음

if value in list: #입력한 값이 리스트에 있는지 확인
    index = list.index(value) #있으면 해당 값의 인덱스를 찾음
    list.pop(index) #리스트에서 값을 삭제
    print("삭제한 인덱스 :", index) #삭제한 값의 인덱스를 출력
    print("삭제 후 리스트 : ", list) #삭제한 후 리스트를 출력
else :
    print("입력한 값이 리스트에 없음") #입력한 값이 리스트에 없을 경우 출력