try:
    a = 1 / 0
except ZeroDivisionError as e:   # ← 여기서 앞에 공백 없애야 함
    print(e)