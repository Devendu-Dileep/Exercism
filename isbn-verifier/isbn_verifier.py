import string


def calculating_value(isbn):
    i=10
    sum = 0
    for dig in isbn[:9]:
        sum += int(dig)*i
        i -= 1
    if isbn[-1] in string.digits:
        return (sum + int(isbn[-1])) % 11 == 0
    elif isbn[-1] == 'X':
        return (sum + 10) % 11 == 0
    return False

def is_valid(isbn):
    isbn_cleaned=isbn.replace('-',"")
    check = len(isbn_cleaned) == 10 and all(c in string.digits for c in isbn_cleaned[:9])
    if check:
        return calculating_value(isbn_cleaned)
    return False    