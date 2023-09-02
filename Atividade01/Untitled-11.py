
pesolimite = 50
peso = float(input("Digite o peso de peixes em quilos: "))

if peso > pesolimite:
    excesso = peso - pesolimite
    multa = excesso * 4.0
else:
    excesso = 0
    multa = 0.0

print("======= Dados do Programa =======")
print("Peso de peixes: {} kg".format(peso))
print("Excesso de peso: {} kg".format(excesso))
print("Multa a pagar: R$ {:.2f}".format(multa))
print("=================================")
