def is_armstrong(number):
    sum = 0 
    data = [num for num in str(number)]
    for i in data:
        sum += int(i)**int(len(data))
    if sum != number:
        return False
    else:
        return True
