import menu
import lancamentos
import consultas
import orcamentos
import edicao
import relatorios


def iniciar_sistema():
    # Estruturas centralizadas mantidas na memória
    lista_lancamentos = []
    dicionario_orcamentos = {}

    while True:
        opcao = menu.exibir_menu()

        if opcao == "1":
            # 1. Cadastrar Lançamentos
            lancamentos.lancamentos(lista_lancamentos)

        elif opcao == "2":
            # 2. Consultas
            consultas.menu_consulta(lista_lancamentos)

        elif opcao == "3":
            # 3. Orçamentos e Limites
            orcamentos.executar(lista_lancamentos, dicionario_orcamentos)

        elif opcao == "4":
            # 4. Editar ou Remover Lançamentos
            edicao.executar(lista_lancamentos)

        elif opcao == "5":
            # 5. Relatório Financeiro
            relatorios.executar(lista_lancamentos)

        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()