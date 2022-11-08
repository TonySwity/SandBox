def calculate(x: float, y: float, operation : str = 'a') -> None:

    def addition(a, b):
        print(a+b)

    def subtraction(a, b):
        print(a-b)

    def division(a, b):
        if b == 0:
            print("На ноль делить нельзя!")
        else:
            print(a/b)

    def multiplication(a, b):
        print(a*b)

    if operation == 'a':
        addition(x,y)
    elif operation == 's':
        subtraction(x,y)
    elif operation == 'd':
        division(x,y)
    elif operation == 'm':
        multiplication(x,y)
    else:
        print("Ошибка. Данной операции не существует")
