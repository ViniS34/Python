'''
Faça um programa que mostre o resultado de n!

5! = 5 * 4 * 3 * 2 * 1
'''

n = int(input("Digite um numero para n: \n"))
fatorial = 1
for i in range (n, 0, -1):
    fatorial = fatorial * i

print(fatorial)

