def calculator(a, b, op):
    if op == '+':
        print(f"{a} + {b} = {a+b}")
    elif op == '-':
        print(f"{a} - {b} = {a-b}")
    elif op == '*':
        print(f"{a} * {b} = {a*b}")
    elif op == '/':
        if b != 0:
            print(f"{a} / {b} = {a/b}")
        else:
            print("0으로 나눌 수 없습니다.")
    else:
        print("지원하지 않는 연산자입니다.")
        

if __name__ == "__main__":
    calculator(2, 2, "+")
    calculator(7, 3, "-")
    calculator(3, 4, "*")
    calculator(6, 5, "/")
    calculator(5, 0, "/")
    calculator(4, 2, ">")