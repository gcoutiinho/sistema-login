from auth import criar_conta, entrar_conta
from menu import menu

def main():
    usuarios = {}

    while True:
        menu()

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("\nDigite um número válido!")
            continue
    
        if opcao == 1:
            criar_conta(usuarios)
        elif opcao == 2:
            entrar_conta(usuarios)
        elif opcao == 3:
            print("\nSaindo....")
            break
        else:
            print("\nOpção Inválida!")
        
main()