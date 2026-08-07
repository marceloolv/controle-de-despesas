import menu
import lancamentos
import orcamentos
import consultas

def iniciar_sistema():

    lista_geral = []

    while True:
        opcao = menu.exibir_menu()

        if opcao == "1":
            novos_dados = lancamentos.lancamentos()
            lista_geral.extend(novos_dados)

        elif opcao == "2":
            consultas.menu_consulta(lista_geral)

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