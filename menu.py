# Supondo que as importações dos outros arquivos aconteçam aqui
# from lancamentos import lancamentos
# from consulta import menu_consulta

def exibir_menu():
    print("\n" + "=" * 36)
    print("         CONTROLE DE DESPESAS")
    print("=" * 36)
    print("1 - Cadastrar Lançamento (Receita/Despesa)")
    print("2 - Acessar Módulo de Consultas")
    print("0 - Sair")
    print("=" * 36)


def principal():
    lista_geral_lancamentos = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            # Chama a função de cadastro e adiciona os novos dados à lista principal
            novos_lancamentos = lancamentos()
            lista_geral_lancamentos.extend(novos_lancamentos)

        elif opcao == "2":
            # Passa a lista atualizada para o menu de consultas
            menu_consulta(lista_geral_lancamentos)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    principal()