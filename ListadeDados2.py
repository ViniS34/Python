print("************")

x = []

for i in range(1, 1001):
    print(i)

print("\n************")

x = [1, 2, 3, 4, 5]
print(x)

y = int(input("Digite um numero para apagar da lista"))

if y in x:
    x.remove(y)
    print("O Valor foi removido com sucesso")

print(x)

print("\n************")

x = [["Vinicius", 18] , ["Felipe", 32] , ["Pedro", 24]]
print(x[0])
print(x[0][0])
print(x[0][1])
print(x[2])
print(x[2][0])
print(x[2][1])

