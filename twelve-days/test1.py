from sys import getsizeof

def testf():
    return iter([i for i in range(1,10) if i % 2 == 0])
    


print(testf())
x = testf()
print(next(x))
print(next(x))
 



