from datetime import datetime

def lancamentos(lista_lancamentos):
    # Gera o próximo código com base no tamanho da lista
    codigo_atual = len(lista_lancamentos) + 1

    while True:
        print("\n=== Cadastro de Receitas e Despesas ===")

        # Tipo
        while True:
            tipo = input("Tipo => [R] Receita, [D] Despesa  [S] Sair): ").strip().lower()
            if tipo in ("r", "d"):
                tipo = "receita" if tipo == "r" else "despesa"
                break
            if tipo == "s":
                return lista_lancamentos

            print("Erro: informe [R] para Receita, [D] para Despesa ou [S] para Sair.")

        # Categoria
        categoria = input("Categoria (ex: salario, alimentacao, transporte): ").strip()

        # Descrição
        descricao = input("Descrição: ").strip()

        # Valor
        while True:
            try:
                valor = float(input("Valor: R$ ").replace(",", "."))
                if valor > 0:
                    break
                print("Erro: O valor deve ser maior que zero.")
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

        # Armazena o lançamento na lista compartilhada
        lista_lancamentos.append({
            "codigo": codigo_atual,
            "tipo": tipo,
            "categoria": categoria,
            "descricao": descricao,
            "valor": valor,
            "data": data
        })

        codigo_atual += 1

        # Continuar?
        continuar = input("\nDeseja cadastrar outro lançamento? (s/n): ").strip().lower()
        if continuar != "s":
            break

    # Resumo do cadastro atual
    print("\n=== Resumo dos Lançamentos ===")
    total_receitas = 0
    total_despesas = 0

    for item in lista_lancamentos:
        print(
            f"Cód: {item['codigo']:<3} | "
            f"{item['data']} | "
            f"{item['tipo'].capitalize():8} | "
            f"{item['categoria'].capitalize():12} | "
            f"{item['descricao']:20} | "
            f"R$ {item['valor']:.2f}"
        )

        if item["tipo"] == "receita":
            total_receitas += item["valor"]
        else:
            total_despesas += item["valor"]

    saldo = total_receitas - total_despesas

    print("\n=== Totais ===")
    print(f"Receitas: R$ {total_receitas:.2f}")
    print(f"Despesas: R$ {total_despesas:.2f}")
    print(f"Saldo:    R$ {saldo:.2f}")

    return lista_lancamentos