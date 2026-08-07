import menu
import lancamentos
import consultas
import orcamentos
import edicao
import relatorios


def iniciar_sistema():
    lista_lancamentos = []
    dicionario_orcamentos = {}

    while True:
        opcao = menu.exibir_menu()

        if opcao == "1":
            # Cadastra novos lançamentos e guarda na lista geral
            novos = lancamentos.lancamentos()
            if novos:
                # Evita duplicar se a função retornar a lista completa
                for item in novos:
                    if item not in lista_lancamentos:
                        lista_lancamentos.append(item)

        elif opcao == "2":
            # Módulo de Consultas
            consultas.menu_consulta(lista_lancamentos)

        elif opcao == "3":
            # Módulo de Orçamentos
            orcamentos.executar(lista_lancamentos, dicionario_orcamentos)

        elif opcao == "4":
            # Módulo de Edição e Remoção
            edicao.executar(lista_lancamentos)

        elif opcao == "5":
            # Módulo de Relatórios
            relatorios.executar(lista_lancamentos)

        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()