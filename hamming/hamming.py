def distance(strand_a, strand_b):

    distance = []
    available = []
    dataA = [a for a in strand_a] 
    dataB = [b for b in strand_b]


    if len(dataA) != len(dataB):
            raise ValueError("The distance are not equal")   

    for a, b in zip(dataA,dataB):             
        
        if a !=  b:
            distance.append(a)

        else:
            available.append(a)

    return len(distance)                  


         

