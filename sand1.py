def generate_fizz_buzz_list(x):
    temp_list = []
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            temp_list.append('FizzBuzz')
        elif i % 3 == 0:
            temp_list.append('Fizz')
        elif i % 5 == 0:
            temp_list.append('Buzz')
        else:
            temp_list.append(i)
    return temp_list


print(generate_fizz_buzz_list(15))
