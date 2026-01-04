def criar_conta(usuarios):
    
    while True:
        print("\n----- SIGN UP -----")
        username = str(input("Nome de usuário: "))
        if not username.strip():
            print("O nome de usuário não pode ser vázio!")
            continue

        senha = str(input("Senha: "))
        if not senha.strip():
            print("Sua senha não pode ser vazia!")
            continue

        nome = str(input("Como deseja ser chamado: "))

        if username in usuarios:
            print(f"O nome {username} já está sendo usado")
            continue
        else:
            usuarios[username] = {
                "senha": senha,
                "nome": nome
            }
            
            print("\nCadastro realizado com sucesso!")
            break

def entrar_conta(usuarios):

    i = 3

    while i > 0:
        print("\n----- SIGN IN -----")
        username = input("Nome de usuário: ")
        senha = input("Senha: ")

        
        
        if username in usuarios:
            if senha == usuarios[username]["senha"]:
                print(f"\nSeja bem vindo(a) {usuarios[username]["nome"]}")
                break
            else:
                i -= 1
                print("\nSenha Inválida!")
                if i == 0:
                    print("Acabou suas tentativas")
                else:
                    print(f"Você tem mais {i} tentativas")
                    continue
        else:
            i -= 1
            print("\nUsuário Inválido!")
            if i == 0:
                print("Acabou suas tentativas")
            else:
                print(f"Você tem mais {i} tentativas")
                continue