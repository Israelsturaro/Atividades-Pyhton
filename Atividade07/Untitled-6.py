
grupopessoas = {}
for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    telefone = input("Digite o número de telefone da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    print("------------------------------------------------------")
   
    grupopessoas[nome] = {"Telefone": telefone, "Idade": idade}

print("Informações de todas as pessoas:")
for nome, info in grupopessoas.items():
    print(f"Nome: {nome}")
    print(f"Telefone: {info['Telefone']}")
    print(f"Idade: {info['Idade']}")
    print()
nomepes = input("Digite o nome da pessoa para visualizar suas informações: ")
if nomepes in grupopessoas:
    infopessoa = grupopessoas[nomepes]
    print(f"Informações da pessoa {nomepes}:")
    print(f"Telefone: {infopessoa['Telefone']}")
    print(f"Idade: {infopessoa['Idade']}")
else:
    print(f"A pessoa {nomepes} não está no grupo.")