def exibir_menu():
    print("\n" + "=" * 36)
    print("         CONTROLE DE DESPESAS")
    print("=" * 36)
    # --- opcoes do menu ---
    print("1 - Lançamentos (Cadastrar)")
    print("2 - Consultas (Buscar / Filtrar)")
    print("3 - Orçamentos (Limites)")
    print("4 - Editar ou Remover Lançamentos")
    print("5 - Relatório Financeiro")
    print("0 - Sair")
    print("=" * 36)

    return input("Escolha uma opção: ").strip()