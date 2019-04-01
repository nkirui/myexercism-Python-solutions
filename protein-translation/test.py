strand ="123456789"

data =[(strand[i:i+3]) for i in range(0, len(strand),3)]


print(data)

