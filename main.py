import menu
import lancamentos
import consultas
import orcamentos
import relatorios


def iniciar_sistema():
    while True:
        # Chama a função do arquivo menu.py
        opcao = menu.exibir_menu()

        if opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        elif opcao == "1":
           ...# lancamentos.executar()
        elif opcao == "2":
           ... # consultas.executar()
        elif opcao == "3":
           ...# orcamentos.executar()
        elif opcao == "4":
           ... # relatorios.executar()
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
