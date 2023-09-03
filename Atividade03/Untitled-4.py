i = 0
while i < 1:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha == nome_usuario:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.\n")
        i +=1
    else:
        print("Nome de usuário e senha cadastrados com sucesso!")
       
