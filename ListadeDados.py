'''
append
insert(0, "x")
pop(1)
remove("x")
len()
sort()
reverse

----------

max()
min()
sum()

'''

print("************")

idade = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20]
idade.append(22)
print(idade)

print("\n************")

idade = [1, 2, 3, 4, 5]
idade.insert(3, "caio")
print(idade)

print("\n************")

idade = [1, 2, 3, 4, 5 ]
print(idade)
idade.pop(2)
print(idade)

print("\n************")

idade = [1, 2, 3, 4, 5 ]
print(idade)
idade.remove(4)
print(idade)

print("\n************")

idade = [1, 2, 3, 4, 5 ]
print(len(idade))

print("\n************")

idade = [4, 6, 8, 9, 3, 4, 6, 1, 2, 3, 4, 5, 0, 7, 10 ]
print(idade)
idade.sort()
print(idade)

print("\n************")

idade = [4, 6, 8, 9, 3, 4, 6, 1, 2, 3, 4, 5, 0, 7, 10 ]
print(idade)
idade.sort(reverse = True)
print(idade)

print("\n************")

idade = [4, 6, 8, 9, 3, 4, 6, 1, 2, 3, 4, 5, 0, 7, 10 ]
print(max(idade))
print(min(idade))
print(sum(idade))