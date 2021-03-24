str = "vinicius silva de chaves"
str = str.upper()
print(str)

str = "VINICIUS SILVA DE CHAVES"
str = str.lower()
print(str)

str = "vinicius"
print(len(str))

str = "vinicius silva"
str = str.replace("silva","chaves")
print(str)

str = "ccc bb eeee"
print(str.count("e"))

str = "Ola, Bem-vindo ao meu Mundo."
str = str.find("Bem-vindo")
print(str)

str = "Ola, Bem-vindo ao meu Mundo."
str = str.find("e")
print(str)

str = "Ola, Bem-vindo ao meu Mundo."
str = str.find("e", 5, 7)
print(str)

str = "Ola, Bem-vindo ao meu Mundo."
str = str.title()
print(str)