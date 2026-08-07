def gerar_relatorio(lancamentos: list) -> None:
    """Exibe um relatório financeiro geral com totais, maiores gastos e alertas.

    Args:
        lancamentos (list): Lista de dicionários contendo os dados dos
          lançamentos.
    """
    # 1. Tratamento para lista vazia ou None
    if not lancamentos:
        print("\n" + "=" * 45)
        print("          RELATÓRIO FINANCEIRO")
        print("=" * 45)
        print("Nenhum lançamento cadastrado para gerar o relatório.")
        print("=" * 45)
        return

    total_receitas = 0.0
    total_despesas = 0.0
    maior_despesa = None
    gastos_categoria = {}

    # 2. Processamento e cálculo das métricas
    for item in lancamentos:
        # Garante que os valores numéricos sejam tratados corretamente
        try:
            valor = float(item.get("valor", 0))
        except (ValueError, TypeError):
            continue

        tipo = item.get("tipo", "").strip().lower()

        if tipo == "receita":
            total_receitas += valor

        elif tipo == "despesa":
            total_despesas += valor

            # Identifica a maior despesa individual
            if maior_despesa is None or valor > maior_despesa.get("valor", 0):
                maior_despesa = item

            # Acumula os gastos por categoria
            categoria = item.get("categoria", "geral").strip().lower()
            gastos_categoria[categoria] = (
                gastos_categoria.get(categoria, 0.0) + valor
            )

    # Cálculo do saldo final
    saldo = total_receitas - total_despesas

    # Identifica a categoria de maior gasto
    if gastos_categoria:
        categoria_maior = max(gastos_categoria, key=gastos_categoria.get)
        valor_categoria = gastos_categoria[categoria_maior]
    else:
        categoria_maior = "Nenhuma"
        valor_categoria = 0.0

    # 3. Exibição formatada do relatório
    print("\n" + "=" * 45)
    print("          RELATÓRIO FINANCEIRO")
    print("=" * 45)
    print(f"Total de Receitas : R$ {total_receitas:10.2f}")
    print(f"Total de Despesas : R$ {total_despesas:10.2f}")
    print(f"Saldo             : R$ {saldo:10.2f}")

    if maior_despesa:
        desc = maior_despesa.get("descricao", "Sem descrição")
        cat = maior_despesa.get("categoria", "Geral").capitalize()
        val = maior_despesa.get("valor", 0.0)
        print("\n--- Maior Despesa ---")
        print(f"Descrição : {desc}")
        print(f"Categoria : {cat}")
        print(f"Valor     : R$ {val:.2f}")

    print("\n--- Categoria de Maior Gasto ---")
    print(f"Categoria : {categoria_maior.capitalize()}")
    print(f"Total     : R$ {valor_categoria:.2f}")

    print("\n--- Situação Financeira ---")
    if saldo < 0:
        print("*** ALERTA: SALDO NEGATIVO! ***")
    elif saldo == 0:
        print("Atenção: Saldo zerado.")
    else:
        print("Saldo positivo.")

    print("=" * 45)


def executar(lancamentos: list) -> None:
    """Função de entrada/interface do módulo chamada pelo menu principal.

    Args:
        lancamentos (list): Lista geral de lançamentos.
    """
    gerar_relatorio(lancamentos)