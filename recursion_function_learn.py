def add_brackets(text: str):
    if len(text) == 1 or len(text) == 2:
        return text
    return text[0] + '(' + add_brackets(text[1:-1]) + ')' + text[-1]


print(add_brackets("Anton"))