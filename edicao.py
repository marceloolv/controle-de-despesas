def editar_lancamento(lancamentos):
    if not lancamentos:
        print("\nNenhum lançamento cadastrado para editar.")
        return

    print("\n=== Editar Lançamento ===")
    for i, item in enumerate(lancamentos, 1):
        cat = item.get("categoria", "geral")
        print(
            f"{i}. {item['data']} | {item['tipo'].capitalize()} | {item['descricao']} | R$ {item['valor']:.2f} | Categoria: {cat}")

    try:
        indice = int(input("\nInforme o número do lançamento a editar: ")) - 1
        if indice < 0 or indice >= len(lancamentos):
            print("Erro: Opção inválida.")
            return
    except ValueError:
        print("Erro: Digite um número válido.")
        return

    item = lancamentos[indice]
    print("\nDeixe o campo em branco para manter o valor atual.")

    # Tipo
    novo_tipo = input(f"Tipo (receita/despesa) [{item['tipo']}]: ").strip().lower()
    if novo_tipo in ("receita", "despesa"):
        item["tipo"] = novo_tipo

    # Descrição
    nova_desc = input(f"Descrição [{item['descricao']}]: ").strip()
    if nova_desc:
        item["descricao"] = nova_desc

    # Categoria
    nova_cat = input(f"Categoria [{item.get('categoria', 'geral')}]: ").strip().lower()
    if nova_cat:
        item["categoria"] = nova_cat

    # Valor
    novo_valor = input(f"Valor [{item['valor']:.2f}]: R$ ").strip().replace(",", ".")
    if novo_valor:
        try:
            val = float(novo_valor)
            if val > 0:
                item["valor"] = val
            else:
                print("Erro: Valor deve ser maior que zero. Mantido valor antigo.")
        except ValueError:
            print("Erro: Valor inválido. Mantido valor antigo.")

    print("Lançamento atualizado com sucesso!")


def remover_lancamento(lancamentos):
    if not lancamentos:
        print("\nNenhum lançamento cadastrado para remover.")
        return

    print("\n=== Remover Lançamento ===")
    for i, item in enumerate(lancamentos, 1):
        print(f"{i}. {item['data']} | {item['tipo'].capitalize()} | {item['descricao']} | R$ {item['valor']:.2f}")

    try:
        indice = int(input("\nInforme o número do lançamento a remover: ")) - 1
        if indice < 0 or indice >= len(lancamentos):
            print("Erro: Opção inválida.")
            return
    except ValueError:
        print("Erro: Digite um número válido.")
        return

    item = lancamentos[indice]

    # Confirmação obrigatória
    confirmacao = input(f"Tem certeza que deseja remover '{item['descricao']}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        lancamentos.pop(indice)
        print("Lançamento removido com sucesso!")
    else:
        print("Remoção cancelada.")