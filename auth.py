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

    tentativas = 3

    while tentativas > 0:
        print("\n----- SIGN IN -----")
        print(f"(Você tem {tentativas} tentativas)")
        username = input("\nNome de usuário: ")
        senha = input("Senha: ")

        if username not in usuarios:
            tentativas -= 1
            print("\nUsuário Inválido!")
            continue

        if senha != usuarios[username]['senha']:
            tentativas -= 1
            print("\nSenha Inválida!")
            continue
        
        print(f"\nSeja bem vindo(a) {usuarios[username]['nome']}")
        return username

    print("\nAcabaram as tentativas...")
    return None