def exibir_tabela(lista_resultados):
    """Função auxiliar para imprimir os lançamentos formatados."""
    if not lista_resultados:
        print(" Nenhuma movimentação encontrada com esses critérios.")
        return

    print(f"{'CÓDIGO':<8} | {'DATA':<10} | {'TIPO':<8} | {'CATEGORIA':<15} | {'DESCRIÇÃO':<20} | {'VALOR'}")
    print("-" * 85)
    for item in lista_resultados:
        print(
            f"{item.get('codigo', '-'):<8} | "
            f"{item.get('data', '-'):<10} | "
            f"{item.get('tipo', '-').capitalize():<8} | "
            f"{item.get('categoria', '-').capitalize():<15} | "
            f"{item.get('descricao', '-'):<20} | "
            f"R$ {item.get('valor', 0):.2f}"
        )


def listar_movimentacoes(lancamentos):
    """Lista todas as movimentações cadastradas."""
    print("\n=== Todas as Movimentações ===")
    exibir_tabela(lancamentos)


def buscar_movimentacoes(lancamentos):
    """Busca por código exato ou por parte da descrição."""
    print("\n=== Buscar Movimentações ===")
    termo = input("Digite o código ou parte da descrição: ").strip().lower()

    resultados = []
    for item in lancamentos:
        codigo_str = str(item.get("codigo", "")).lower()
        descricao_str = item.get("descricao", "").lower()

        # Verifica se o termo é exatamente o código ou se está contido na descrição
        if termo == codigo_str or termo in descricao_str:
            resultados.append(item)

    exibir_tabela(resultados)


def filtrar_movimentacoes(lancamentos):
    """Filtra por tipo (receita/despesa) e/ou categoria."""
    print("\n=== Filtrar Movimentações ===")

    tipo_filtro = input("Qual tipo deseja filtrar? (receita/despesa ou deixe em branco para ignorar): ").strip().lower()
    categoria_filtro = input("Qual categoria deseja filtrar? (ou deixe em branco para ignorar): ").strip().lower()

    resultados = []
    for item in lancamentos:
        # Se o usuário deixou em branco, a condição é validada como True (ignora o filtro)
        match_tipo = (not tipo_filtro) or (item.get("tipo", "") == tipo_filtro)
        match_categoria = (not categoria_filtro) or (categoria_filtro in item.get("categoria", "").lower())

        if match_tipo and match_categoria:
            resultados.append(item)

    exibir_tabela(resultados)


def menu_consulta(lancamentos):
    """Menu principal do módulo de consultas."""
    while True:
        print("\n" + "=" * 30)
        print("      MENU DE CONSULTAS")
        print("=" * 30)
        print("1. Listar todas as movimentações")
        print("2. Buscar por código ou descrição")
        print("3. Filtrar por tipo e categoria")
        print("4. Voltar / Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_movimentacoes(lancamentos)
        elif opcao == "2":
            buscar_movimentacoes(lancamentos)
        elif opcao == "3":
            filtrar_movimentacoes(lancamentos)
        elif opcao == "4":
            print("Saindo do menu de consultas...")
            break
        else:
            print("Opção inválida! Tente novamente.")

#
# # ==============================================================================
# # ÁREA DE TESTE (Você pode remover isso quando for juntar com o código principal)
# # ==============================================================================
# if __name__ == "__main__":
#     # Dados fictícios com os novos campos (codigo e categoria) para você testar
#     dados_teste = [
#         {"codigo": 1, "tipo": "receita", "categoria": "salario", "descricao": "Salario da empresa", "valor": 3500.00,
#          "data": "05/10/2023"},
#         {"codigo": 2, "tipo": "despesa", "categoria": "alimentacao", "descricao": "Almoco no shopping", "valor": 45.50,
#          "data": "06/10/2023"},
#         {"codigo": 3, "tipo": "despesa", "categoria": "transporte", "descricao": "Uber para o trabalho", "valor": 15.00,
#          "data": "07/10/2023"},
#         {"codigo": 4, "tipo": "receita", "categoria": "freelance", "descricao": "Projeto de frontend", "valor": 800.00,
#          "data": "10/10/2023"}
#     ]
#
#     menu_consulta(dados_teste)