
n1 = float  (input("Informe a primeira nota: "))
n2 = float (input("Informe a segunda nota: "))
n3 = float (input("Informe a terceira nota: "))
n4 = float (input("Informe a quarta nota: "))

media = (n1+n2+n3+n4)/4

if media >= 7:
    print("Aprovado")
elif media > 5:
    print("Recuperação")
else:
    print("Reprovado")
    
print("-----------------------------")
print(f"Sua media será: {media:.2f}")
print("-----------------------------")