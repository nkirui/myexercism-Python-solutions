def classify(number):
    if number < 1:
        raise ValueError("less than 1 not accepted")
    factors = sum([ i for i in range(1,number+1) if number % i == 0 ][:-1])
    
    if factors == number:
        return ("perfect") 
    if factors > number:
        return ("abundant") 
    if factors < number:
        return ("deficient") 
    
    # Very slow algorithm the test takes (Ran 13 tests in 17.765s)
    """factors = [ i for i in range(1,number+1) if number % i == 0 ][:-1]
    while number > 0:
        if sum(factors) == number:
            return ("perfect")
        elif sum(factors) > number:
            return ("abundant")
        elif sum(factors) < number:
            return("deficient")
        else:
            raise ValueError("Neither")
    else:
        raise ValueError("Negative numbers are not acceptable")"""


