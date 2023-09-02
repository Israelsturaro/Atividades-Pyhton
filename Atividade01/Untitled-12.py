
valorhora = float(input("Digite o valor que você ganha por hora: "))
horastrabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salariobruto = valorhora * horastrabalhadas
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - ir - inss - sindicato

print("======= Dados da Empresa =======")
print("+ Salário Bruto: R$ {:.2f}".format(salariobruto))
print("- IR (11%): R$ {:.2f}".format(ir))
print("- INSS (8%): R$ {:.2f}".format(inss))
print("- Sindicato (5%): R$ {:.2f}".format(sindicato))
print("+ Salário Líquido: R$ {:.2f}".format(salarioliquido))
print("=================================")
