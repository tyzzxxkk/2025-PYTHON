count = 0

for i in range(1, 101):
    for ch in str(i):
        if ch in '369':
            count += 1

print("박수 친 횟수 :", count)
