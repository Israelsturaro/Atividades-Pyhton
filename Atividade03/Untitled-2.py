

n1 = float (input("Informe os pontos  jogador 01: "))
n2 = float (input("Informe os pontos  jogador 02: "))
n3 = float (input("Informe os pontos  jogador 03: "))

soma = n1 + n2 + n3 
print("----Dados da Equipe------")

if n1 > n2 and n1 > n3:
    print("",n1,n2,n3)    
    
elif n2 > n1 and n2 > n3:
    print("",n2,n1,n3)    
     
elif n3 > n1 and n3 > n2:
    print("", n3,n2,n1)    
     
elif n1 > n2 and n1 < n3:
    print("",n1,n2,n3)
        
## Media aritimedica
if soma >= 100:
    print(f"Media: {(n1 + n2 + n3)/3:.1f}")
else:
    print("Equipe Desclassificada")