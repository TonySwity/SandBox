a, b, *c = [1,2,3,4,5,6,7]

print(a, b, c)


def f(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


f(a=1, b=2, c=3)


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(5))


def polindrom(text: str) -> bool:
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return polindrom(text[1:-1])


print("texet"[1:-1])


def print_to(num: int):
    if num > 0:
        print_to(num-1)
        print(num)


print_to(5)


def double_fact(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    return double_fact(x - 2) * x


print(double_fact(6))


def tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


print(tribonacci(7))


def fact(x):
    if x == 1:
        return 1

    return fact(x-1)*x


def get_combin(n: int, k: int) -> int:
    if k == 0:
        return 1
    if n == k:
        return 1

    return fact(n)//(fact(k)*fact(n-k))


print(get_combin(5,2))