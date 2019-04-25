def is_isogram(string):  

    data= "".join(sorted([i.upper() for i in string if i.isalpha()])).strip()

    data2= "".join(sorted({i.upper()for i in string if i.isalpha()})).strip()

    if data != data2:
        return False
    else:
        return True   

