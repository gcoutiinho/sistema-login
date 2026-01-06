def ver_perfil(usuarios, username):
    print("\n----- PERFIL -----")
    print(f"\nUsername: {username}")
    print(f"Nome: {usuarios[username]['nome']}")

def alterar_senha(usuarios, username):

    print("\n----- ALTERAR SENHA -----")

    senha_atual = input("Digite sua senha atual: ")

    if senha_atual != usuarios[username]['senha']:
        print("Senha incorreta!")
        return

    nova_senha = input("\nDigite a nova senha: ")
    usuarios[username]['senha'] = nova_senha
    print("Senha alterada com sucesso!")