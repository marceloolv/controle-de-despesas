def executar(lancamentos, orcamentos):
    while True:
        print("\n" + "=" * 36)
        print("          ORÇAMENTOS")
        print("=" * 36)
        print("1 - Definir limite por categoria")
        print("2 - Comparar gastos com limite")
        print("0 - Voltar")
        print("=" * 36)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            definir_limite_categoria(orcamentos)
        elif opcao == "2":
            comparar_gastos_com_limite(lancamentos, orcamentos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def definir_limite_categoria(orcamentos):
    print("\n=== Definir Limite por Categoria ===")
    categoria = input("Informe a categoria: ").strip().lower()

    if not categoria:
        print("Erro: A categoria não pode ser vazia.")
        return

    while True:
        try:
            limite = float(input(f"Limite mensal para '{categoria}': R$ ").replace(",", "."))
            if limite > 0:
                break
            print("Erro: O limite deve ser maior que zero.")
        except ValueError:
            print("Erro: Informe um valor numérico válido.")

    orcamentos[categoria] = limite
    print(f"Limite para '{categoria}' cadastrado: R$ {limite:.2f}")


def comparar_gastos_com_limite(lancamentos, orcamentos):
    print("\n=== Comparativo de Orçamento vs Gasto ===")

    if not orcamentos:
        print("Nenhum orçamento cadastrado até o momento.")
        return

    gastos_categoria = {}
    for item in lancamentos:
        if item.get("tipo") == "despesa":
            cat = item.get("categoria", "geral").lower()
            gastos_categoria[cat] = gastos_categoria.get(cat, 0.0) + item["valor"]

    for cat, limite in orcamentos.items():
        gasto = gastos_categoria.get(cat, 0.0)
        porcentagem = (gasto / limite) * 100 if limite > 0 else 0

        status = "OK"
        if gasto > limite:
            status = "EXTORADO!"
        elif gasto >= limite * 0.8:
            status = "ALERTA (>= 80%)"

        print(
            f"Categoria: {cat.capitalize():12} | Gasto: R$ {gasto:8.2f} / R$ {limite:8.2f} ({porcentagem:5.1f}%) | Status: {status}"
        )