
i = gordo = magro = 0
for i in range(2):
    identificação = int (input(f"Digite a identifivação do N°{i + 1}: "))
    peso = int(input(f"Digite o peso do Boi{i + 1}: "))
    print("------------------------------------------------------")
    i+= 1
    
    if peso > gordo:
        gordo = peso
    else:
        print("")

    if peso > magro:
        magro = peso 
    else:
        print("")
print("Boi mais pesado: ", gordo)
print("Boi mais magro: ",magro)


