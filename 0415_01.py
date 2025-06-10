#모래시계 별찍기

n = int(input())

if n%2 == 0:
    n-=1

for i in range(n//2 , 1, -1):
    print(" "*(n-i) + "*"*(i*2-1))

for i in range(1, n//2 +1):
    print(" "*(n-i) + "*"*(i*2-1))