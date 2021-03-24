'''
max()
min()
sum()
print()

'''

def mostrarNaTela():
    print("Ola Mundo!")
    print("fim do programa..")

mostrarNaTela()

def somaNumeros(n1, n2):
    print(f"A Soma dos números é {n1 + n2}")

somaNumeros(10, 20) 
''' Ou, n1 = 10 , n2 = 20 '''

def retornaMaior(*list):
    print(list)
    print(max(list))
    print(min(list))

retornaMaior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
