def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    try:
        number=int(number)
        if number<1:
            raise ValueError("Classification is only possible for positive integers.")
        list_of_factors=[i for i in range(1,number) if number%i==0]
        return ("perfect" if sum(list_of_factors)==number else "deficient" if sum(list_of_factors)<number else "abundant")
    except (ValueError, TypeError) as e:
        raise
    

'''for i in range(1,number):
            if number%i==0:
                list_of_factors=i
        if sum(list_of_factors)==number:
            return "Perfect"
        elif sum(list_of_factors)<number:
            return "Deficient"
        else:
            return "Abundant"'''
    
