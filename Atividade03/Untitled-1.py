

n1 = int (input("Informe a primeiro numero: "))
n2 = int (input("Informe a primeiro segundo: "))
n3 = int (input("Informe a primeiro terceiro: "))

if n1 >n2 and n1 > n3:
    print("",n1)
    
elif n2 > n3 and n2 > n1:
    print("",n2)
    
elif n3 > n1 and  n3 > n2:
    print("",n3) 
else:
    print("numero invalido") 