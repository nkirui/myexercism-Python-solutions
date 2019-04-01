scores = [100,60,90,50,10,70, 20,30]

def personal_top_three(data):

    data.sort(reverse = True)
    return data[:3]
      

print(personal_top_three(scores))


