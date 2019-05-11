days = ("first","a Partridge in a Pear Tree."),("second","two Turtle Doves"), ("third","three French Hens"),("fourth","four Calling Birds"), ("fifth","five Gold Rings"), ("sixth","six Geese-a-Laying"),("seventh","seven Swans-a-Swimming"),("eighth","eight Maids-a-Milking"),("ninth","nine Ladies Dancing"), ("tenth","ten Lords-a-Leaping"),("eleventh","eleven Pipers Piping"),("twelfth","twelve Drummers Drumming")


def recite(start_verse, end_verse):
    iterate=[ value for key,value in days][:end_verse]    
    if len(iterate) > 1:        
        iterate.pop(0)
        iterate = ["and a Partridge in a Pear Tree."] + iterate
    
    for key ,value in enumerate(days,1):
        if key == start_verse:
            return["On the {} day of Christmas my true love gave to me: {}".format(value[0],", ".join(iterate[::-1]))]
            
      
     

print(recite(1,3))



            
    

