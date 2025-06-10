#교과서 133쪽 10번 문제 다시 풀기

def wc(text):
    word_count = len(text.split())
    char_count = len(text)
    whitespace = text.count(' ')
    return (word_count, char_count, whitespace)

word_count, char_count, whitespace = wc("파이썬 수업")
print("단어 수 :", word_count, ", 글자 수 :", char_count, ", 공백 수 :", whitespace)