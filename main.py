from auth import criar_conta, entrar_conta
from menus import menu, menu_logado
from usuario import ver_perfil, alterar_senha
from storage import salvar_usuarios, carregar_usuarios

def main():
    usuarios = carregar_usuarios()

    while True:
        menu()

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("\nDigite um número válido!")
            continue
    
        if opcao == 1:
            criar_conta(usuarios)
            salvar_usuarios(usuarios)
        elif opcao == 2:
            usuario_logado = entrar_conta(usuarios)

            if usuario_logado:
                while True:
                    menu_logado()
                    
                    try:
                        opcao = int(input("Escolha: "))
                    except ValueError:
                        print("\nDigite um número válido!")
                    
                    if opcao == 1:
                        ver_perfil(usuarios, usuario_logado)
                    elif opcao == 2:
                        alterar_senha(usuarios, usuario_logado)
                        salvar_usuarios(usuarios)
                    elif opcao == 3:
                        print("\nVoltando ao menu principal...")
                        break
        elif opcao == 3:
            print("\nSaindo....")
            break
        else:
            print("\nOpção Inválida!")
        
main()