def raindrops(number):
    facts =((3, "Pling"),(5,"Plang"),(7,"Plong"))
    return ''.join([s for d,s in facts if number % d == 0]) or str(number) 
