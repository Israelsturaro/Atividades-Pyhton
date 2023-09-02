## Atividade 05
alunos = int (input("Digite quantos alunos tem na sala: "))
aprovado = 0
reprovados = 0
soma = 0
percentual = 0
i = 0
while i < alunos: 
    nota = float(input("Digite a nota: \n"))

    if nota >= 7:
        aprovado+=1
    else:
        reprovados+=1
  
    soma +=nota
    i += 1

print("Quantidade de Aprovados: ", aprovado)
print("Quantidade de Reprovados: ", reprovados) 
print("Media da turma: ", soma / alunos)  
print(f"Percentual de Alunos reprovados: {(reprovados / alunos)*100:.1f}",)       