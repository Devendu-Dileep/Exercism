def square(number):
    try:
        number=int(number)
        if not(1<=number<=64):
            raise ValueError("square must be between 1 and 64")
        return 2**(number-1)
        
    except (ValueError,TypeError) as e:
        raise

def total():
    return (sum([2**(i-1) for i in range(1,65)]))
