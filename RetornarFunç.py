def retorna():
    return 10
a = retorna()
print(a)

def retorna(a , b):
    return a + b
a = retorna(10,50)
print(a)

def retorna():
    return 10, 20
a = retorna()
print(a)


def retorna():
    return 10, 20
a, b = retorna()
print(a)
print(b)