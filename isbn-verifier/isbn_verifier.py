def verify(isbn):
    total = 0
    multi = 10
    isbk= [d for d in isbn if d.isalnum()]
    if len(isbk) != 10:
        return False
    if len(isbk) < 10:
        return False    
    if isbk[-1].upper() == 'X':
        isbk[-1]= str(10) 
    try:
        data = map(int,isbk)              
        for i in data:
            total += i*multi
            multi -= 1
        if total % 11 == 0:
            return True
        else:
            return False
    except :
        return(False)

print(verify("3-598-21507-x"))

 