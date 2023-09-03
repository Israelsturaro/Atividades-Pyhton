i = timefor = timecea = timefer = timeica = timeout = moradiaqtd = moradiaqtd2 = mediaSal = 0
while i < 3:
    time = int(input("Digite qual é seu time: 1- Fortaleza| 2- Ceará| 3- Ferroviario | 4- icasa | 5- outros: "))
    moradia = int(input("Digite sua moradia: 1- Fortaleza| 2- Caucaia| 3- outros: "))
    salario = float(input("Digite seu Salario: "))
    print("----------------------------------------------------------------------------------------------------")
    i += 1
    ##Quantidade de Pessoas torcendo:
    if time == 1:
        timefor+=1
        ##Media salarial
        mediaSal+=salario
    elif time == 2:
        timecea+=1
    elif time == 3:
        timefer+=1
    elif time == 4:
        timeica+=1
    else:
        timeout+=1 
    ##Quantidade Moradores que torcem Fer
    if time == 3 and moradia == 2:
        moradiaqtd += 1
    ##Quantidade Moradores que torcem Ceara e mora em Fortal
    if time == 2 and moradia == 1:
        moradiaqtd2 += 1
print("Quantidade de Torcedores de Cada time: ","Fortaleza: ",timefor,"Ceara: ",timecea,"Ferroviario: ",timefer,"Icasa: ",timeica,"Outros: ",timeout)
print("Media Salarial Do Fortaleza: ",mediaSal / timefor)
print("Quantidade de Pessoas que torcem Ferroviario e moram na caucaia: ", moradiaqtd)
print("Quantidade de Pessoas que torcem Ceara e moram  em Fortal: ", moradiaqtd2)
