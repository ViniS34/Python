x = {"Nome": "Vinícius","Idade": 18,"Telefone": "5532357689452"}
print(x)
print(x["Nome"])
print(x["Idade"])
print(x["Telefone"])
x.pop("Idade")
print(x)
'print(len(x))'

cadastroPessoas = [{"Nome": "Vinicius", "Idade": 18, "Telefone": "554532674586", "CPF": "235687342-76"},
                   {"Nome": "Anderson", "Idade": 24, "Telefone": "555231474383", "CPF": "231787343-56"}]

print(cadastroPessoas)
print(cadastroPessoas[0]["Telefone"])