def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')


quantity = 5
vegetable = 'bananas'
cost = 1.74
f(quantity, vegetable, cost)


def make_header(text: str, headerSize: int = 1):
    return f'<h{headerSize}>{text}</h{headerSize}>'



def create_matrix(size: int = 3, up_fill :int = 0, down_fill: int = 0):
    matrix = [[0]*size for i in range(size)]
    count = 1
    # print(matrix)
    for i in range(size):
        for j in range(size):
            if j>i:
                matrix[i][j] = up_fill
            if j<i:
                matrix[i][j] = down_fill
            if i == j:
                matrix[i][j] = count
                count += 1
    return matrix

print(create_matrix())