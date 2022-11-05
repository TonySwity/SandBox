sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

print(sweet.get('name'), sweet.get('calories'), sweet.get('id'), sep='\n')

sweet.setdefault('weight', 230)
sweet.setdefault('have_topping', True)
sweet['name'] = 'SuperCake'
sweet['calories'] = 350

print(sweet)

del sweet['ppu'], sweet['type']

print(sweet)

# n = int(input())
#
# nums_dict ={}
#
# for i in range(1,n+1):
#     nums_dict.setdefault(i, i**2)
#
# print(nums_dict)

from string import ascii_lowercase

alphabet = {ascii_lowercase[i]: i+1 for i in range(len(ascii_lowercase))}

print(alphabet)


a = [10, 20, 30, 40]
s = 'hello'
t = ('apple', 'banana', 'mango')
d = {'a': 1, 'b': 2, 'c': 3}

print(enumerate(a))
print(list(enumerate(a)))

for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(s):
    print(index, value)

for index, value in enumerate(t):
    print(index, value)

for index, value in enumerate(d):
    print(index, value)

for index, value in enumerate(range(10, 20)):
    print(index, value)

for index, value in enumerate(t, 100):
    print(index, value)

# Algorithm Luna

s = '3942682966937054'
s = s[-1::-1]
evens = 0
odds = sum(int(v) for i, v in enumerate(s, 1) if i % 2 != 0)

for i, v in enumerate(s, 1):
    if i % 2 == 0:
        if (temp := int(v)*2) > 9:
            temp -= 9
            evens += temp
        else:
            evens += int(v)*2

print((evens+odds) % 10 == 0)
# print(sum % 10 == 0)

# evens = sum(int(i) for i in s[-1::-2])
# odds = sum(int(i) for i in s[-2::-2])
# print((evens + odds) % 10 == 0, evens + odds)
#
#
# from functools import reduce
#
# def luhn(code):
#     # Предварительно рассчитанные результаты умножения на 2 с вычетом 9 для больших цифр
#     # Номер индекса равен числу, над которым проводится операция
#     LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
#     code = reduce(str.__add__, filter(str.isdigit, code))
#     evens = sum(int(i) for i in code[-1::-2])
#     odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
#     return ((evens + odds) % 10 == 0, evens, odds)
#
# print("Прошел проверку: ", luhn('4561 2612 1234 5467'))
# print("Не прошел проверку: ", luhn('4561 2612 1234 5464'))

my_tuple = (1, 3.5, 'sisi', True)
my_tuple = ('zara', 'h&m', 'mcdonalds', 'visa', 'ikea')
print(min(my_tuple))

a = (1,)
b = ('R',)
c = ('A',)
d = (2,)
e = a*3 + b*4 + c*7 +d*5
print(e)

my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)

slice_5_10 = my_tuple[5:11]
slice_from_20 = my_tuple[20:]
slice_to_35 = my_tuple[:35]

print(slice_5_10)
print(slice_from_20)
print(slice_to_35)

my_tuple = my_tuple[-1::-1]

print(my_tuple)

my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)

summa = 0
count = 0

for i in my_tuple:
    if i%2 != 0:
        summa += i
        count += 1

print(summa / count)


account = {
  "id": 5681,
  "uid": "45f17b56-bcad-4933-8c73-a37aaa6863b9",
  "account_number": "6733198878",
  "iban": "GB79PNXF20678598570754",
  "bank_name": "AAC CAPITAL PARTNERS LIMITED",
  "routing_number": "007398728",
  "swift_bic": "AACCGB21"
}

print(len(account))


user = {
  "id": 1614,
  "uid": "ed690244-94f3-41ac-82d8-cc2c63a18ed2",
  "password": "Coc0f2A3in",
  "first_name": "Lucien",
  "last_name": "Langworth",
  "username": "lucien.langworth",
  "email": "lucien.langworth@email.com",
  "gender": "Female",
  "phone_number": "+371 296-827-8753 x737",
  "social_insurance_number": "609088166",
  "date_of_birth": "1993-10-14",
}

print('username' in user)
print('u id' in user)

currencies = {
    'Argentine Peso': 118362.205708,
    'Australian Dollar': 1586.232315,
    'Bahraini Dinar': 423.780164,
    'Botswana Pula': 13168.450636,
    'Brazilian Real': 5954.781483,
    'British Pound': 834.954104,
    'Bruneian Dollar': 1520.451015,
    'Bulgarian Lev': 1955.83,
    'Canadian Dollar': 1430.54405,
    'Chilean Peso': 898463.818465,
    'Chinese Yuan Renminbi': 7171.445692,
    'Colombian Peso': 4447741.922165,
    'Croatian Kuna': 7527.744707,
    'Czech Koruna': 24313.797041,
    'Danish Krone': 7440.613895,
    'Emirati Dirham': 4139.182587,
    'Hong Kong Dollar': 8786.255952,
    'Hungarian Forint': 355958.035747,
    'Icelandic Krona': 143603.932438,
    'Indian Rupee': 84241.767127,
    'Indonesian Rupiah': 16187150.010697,
    'Iranian Rial': 47534006.535121,
    'Israeli Shekel': 3569.191411,
    'Japanese Yen': 129149.364679,
    'Kazakhstani Tenge': 489292.515538,
    'Kuwaiti Dinar': 340.959682,
    'Libyan Dinar': 5196.539901,
    'Malaysian Ringgit': 4717.485104,
    'Mauritian Rupee': 49212.933037,
    'Mexican Peso': 23130.471272,
    'Nepalese Rupee': 134850.008728,
    'New Zealand Dollar': 1703.649473,
    'Norwegian Krone': 9953.078431,
    'Omani Rial': 433.360301,
    'Pakistani Rupee': 198900.635421,
    'Philippine Peso': 57574.278782,
    'Polish Zloty': 4579.273862,
    'Qatari Riyal': 4102.552652,
    'Romanian New Leu': 4946.638369,
    'Russian Ruble': 86197.012666,
    'Saudi Arabian Riyal': 4226.530892,
    'Singapore Dollar': 1520.451015,
    'South African Rand': 17159.831129,
    'South Korean Won': 1355490.097163,
    'Sri Lankan Rupee': 228245.645722,
    'Swedish Krona': 10439.125427,
    'Swiss Franc': 1037.792217,
    'Taiwan New Dollar': 31334.286611,
    'Thai Baht': 37436.518169,
    'Trinidadian Dollar': 7636.35428,
    'Turkish Lira': 15078.75981,
    'US Dollar': 1127.074905,
    'Venezuelan Bolivar': 511082584.868731
}
s = input()
print(currencies.get(s, f'Нет данных по {s}'))
# print(*currencies.items(), sep='\n')

account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}

keys = [i for i in account]

print(keys)

a = {1: "one", 2: "two"}
b = {2: "dva", 3: "three"}
c = {3: "tri", 2: "два"}

result = c | a | b
print(result)

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}

v1 = user.pop('password')
v2 = user.pop('last_name')
user.setdefault('secret', v1)
user.setdefault('surname', v2)
print(user)

workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}
workers['employer3']['salary'] += 8000
print(workers)

supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
total = []
for value in supermarket.values():
    s = value["quantity"] * value["price"]
    total.append(s)

print(sum(total))

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}

dict_key_list = input().split()
new_dict = {key:user[key] for key in dict_key_list}

print(new_dict)