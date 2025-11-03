# 리본 별찍기

n = int(input())

if n%2 == 0:
     n-=1

for i in range(1, n//2 + 1):
    print("*"*i +" " * (n - 2 * i)+ "*"*i)

print("*"*n)

for i in range(n//2, 0, -1):
     print("*"*i +" " * (n - 2 * i)+ "*"*i)