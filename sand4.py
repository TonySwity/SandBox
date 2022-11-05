
def count_letter(text: str, letter: str):
    print(text.count(letter))


# numbers = list(map(float, input().split()))
#
# print(sum(numbers) / len(numbers))


# n, a, b = map(int,input().split())
#
# sum = (a*b*n)*2
# print(sum)


allCount = int(input())

x = allCount//6

y = allCount - 2*x

print(x, y, x)