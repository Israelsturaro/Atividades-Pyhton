
n1 = str (input("Informe o nome: "))
n2 = int (input("Informe sua idade: ")) 

if n2 <= 10:
    print("Vai pagar 30R$")
elif n2 > 10:
    print("Vai pagar 60R$")
elif n2 > 29   :
    print("Vai pagar 120R$")
elif n2 > 45:
    print("Vai pagar 150R$")  
elif n2 > 59 and n2 < 65:
    print("Vai pagar 250R$")
else:
    print("Vai pagar 400R$")