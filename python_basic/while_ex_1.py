# 여러 선택 중 하나 선택
prompt = """
    1. 가
    2. 나
    3. 다
    4. 라

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())