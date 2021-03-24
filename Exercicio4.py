'''
Faça um programa que receba várias idades e calcule e mostre a media das idades.
Finalize o programa quando a entrada for igual a -1
'''

x = 0
soma = 0
i = 0
while x != -1:
    x = int(input("Digite uma idade"))
    if x != -1:
        soma += x
        i += 1

print(x)