def on_square(integer_number):
    if integer_number < 1 or integer_number > 64:
        raise ValueError("Not valid number")        
    data = [2**(i-1) for i in range(1,integer_number+1)]
    return int("".join(str(data[-1])).strip('[]'))

def total_after(integer_number):
    if integer_number < 1 or integer_number > 64:
        raise ValueError("Not valid number")
    return sum([2**(i-1) for i in range(1,integer_number+1)])
   
