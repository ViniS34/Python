print("1 \n 1 \n 1 \n 1 \n 1 \n 1 \n 1 \n 1 \n 1 \n 1 ")
print("1111111111")

x = 0
while x < 10:
    print("1")
    x = x + 1
print("Processo de repetição terminado.")

decisao = 0
while decisao != 3:
    decisao = int(input("Digite 1 para realizar o login"
                     "\n Digite 2 para realizar o cadastro" 
                     "\n Digite 3 para sair do processo de registro"))
    
    if decisao == 3:
        break
    if decisao == 1:
        print("Em processo de login..")
    elif decisao == 2:
        print("Em processo de cadastramento..")
print("O processo foi encerrado.")