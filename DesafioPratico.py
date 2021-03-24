print("Sistema da Universidade do Sul de Santa Catarina, Unisul")

nome = "vinicius silva de chaves"
nome = nome.title()
print(f"Nome: {nome}")

idade = 18
print(f"Idade: {idade}")

Prova1 = 7.5
Prova2 = 8.0
Media = (Prova1 + Prova2) / 2

if Media >=6 and idade >=18:
    print(f"O Aluno {nome} foi aprovado!")
else:
    print(f"O Aluno {nome} foi reprovado!")
print("Fim da sessão")
