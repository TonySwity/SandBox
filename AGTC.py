def count_AGTC(dna: str):

    dataChar = {'A': 0, 'G': 0, 'T': 0, 'C': 0}

    for i in dna:
        dataChar[i] = dataChar.setdefault(i, 0) + 1

    return tuple(dataChar.values())


dna = input()

print(count_AGTC(dna))