n = int(input("숫자를 입력하세요 : "))
scores = list(map(int, input().split()))

score_set = set(scores)
unmatched = []

for score in score_set:
    if -score not in score_set:
        unmatched.append(score)

print(sum(unmatched))