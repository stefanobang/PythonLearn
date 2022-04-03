#GuGuDan.py


def GuGu(n):
    result = []
    number = 1
    while number < 10:
        result.append(n*number)
        number += 1
    return result


print(GuGu(2))
