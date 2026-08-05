from datetime import datetime


def lancamentos():
    lancamentos = []

    while True:
        print("\n=== Cadastro de Receitas e Despesas ===")

        # Tipo
        while True:
            tipo = input("Tipo (receita/despesa): ").strip().lower()
            if tipo in ("receita", "despesa"):
                break
            print("Erro: informe 'receita' ou 'despesa'.")

        # Descrição
        descricao = input("Descrição: ").strip()

        # Valor
        while True:
            try:
                valor = float(input("Valor: R$ ").replace(",", "."))
                if valor > 0:
                    break
                print("Erro: o valor deve ser maior que zero.")
            except ValueError:
                print("Erro: informe um valor numérico válido.")

        # Data
        while True:
            data = input("Data (DD/MM/AAAA): ").strip()
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break
            except ValueError:
                print("Erro: data inválida.")

        # Armazena o lançamento
        lancamentos.append({
            "tipo": tipo,
            "descricao": descricao,
            "valor": valor,
            "data": data
        })

        # Continuar?
        continuar = input("\nDeseja cadastrar outro lançamento? (s/n): ").strip().lower()
        if continuar != "s":
            break

    # Resumo
    print("\n=== Resumo dos Lançamentos ===")

    total_receitas = 0
    total_despesas = 0

    for item in lancamentos:
        print(
            f"{item['data']} | "
            f"{item['tipo'].capitalize():8} | "
            f"{item['descricao']:20} | "
            f"R$ {item['valor']:.2f}"
        )

        # Soma os totais
        if item["tipo"] == "receita":
            total_receitas += item["valor"]
        else:
            total_despesas += item["valor"]

    saldo = total_receitas - total_despesas

    print("\n=== Totais ===")
    print(f"Receitas: R$ {total_receitas:.2f}")
    print(f"Despesas: R$ {total_despesas:.2f}")
    print(f"Saldo:    R$ {saldo:.2f}")


# Executa a função
lancamentos()