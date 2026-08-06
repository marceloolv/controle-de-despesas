import menu
import lancamentos
import orcamentos

def iniciar_sistema():
    while True:
        opcao = menu.exibir_menu()

        if opcao == "1":
            lancamentos.lancamentos()

        elif opcao == "2":
            pass

        elif opcao == "3":
            orcamentos.executar()

        elif opcao == "4":
            pass

        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()