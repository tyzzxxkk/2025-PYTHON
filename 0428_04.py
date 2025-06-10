def tokenize(s): # 입력 문자열을 간단히 토큰화하는 함수
    return ['println' if s.startswith('println') else 'print', # 첫 키워드 확인
            'left_paren', s.split('"')[1], 'right_paren', 'semicolon'] # 따옴표 안의 문자열 추출


# 토큰을 실행하여 출력하는 함수
def execute(tokens):
    print(tokens[2], end='\n' if tokens[0] == 'println' else '') # println이면 줄바꿈


# 예시 실행
execute(tokenize('print("a");'))
execute(tokenize('println("b");'))