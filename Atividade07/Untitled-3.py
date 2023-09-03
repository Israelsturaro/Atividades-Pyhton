nome = input("Digite Nome: ")
idade = int(input("Digite idade: "))
telefone = input("Digite telefone: ")
endereço = input("Digite endereço: ")
dict = {
    "nome":nome,
    "idade":idade,
    "telefone":telefone,
    "endereço":endereço}
x = dict.items()
print(x)    