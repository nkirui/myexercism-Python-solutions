def slices(series, length):
    comp = []
    if not series:
        raise ValueError('Serries cannot be empty.')

    if length <= 0 or length > len(series):
        raise ValueError('Length cannot be less or equal to zero nor it cannot be greater the length of series ')
    
    else:
        for i in range(0,len(series)-length+1):
            comp.append(series[i:i+length])
        return comp


    
