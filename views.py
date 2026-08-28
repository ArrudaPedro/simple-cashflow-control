def entrada_dados(nome_controle, campos):
    dados = {}

    print(f"--- {nome_controle}:")
    for campo in campos:
        dados[campo] = input(f"{campo}: ")


    print(f"---- Resumo de {nome_controle}:")
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")


campos_recebimento_diario = ["Despesas", "Fita (Valor Total)", "Comissão", "Voucher"]
dados_recebimento = entrada_dados("Controle de Recebimento Diario", campos_recebimento_diario)

campos_controle_contabil = ["Fornecedor", "Valor", "Número da nota", "Forma de Pagamento", "Data de emissão"]
dados_contabil = entrada_dados("Controle Contabil", campos_controle_contabil)




