def controle_recebimento_diario():
    campos = ["Despesas", "Fita (Valor Total)", "Comissão", "Voucher"]



def controle_contabil():
    campos = ["Fornecedor", "Valor", "Número da nota", "Forma de Pagamento", "Data de emissão"]
    dados = {}


    print("Controle de Contabilidade")

    for campo in campos:
        dados[campo] = input(f"Digite o valor para {campo}: ")

    for campo, valor in dados.items():
        print(f"{campo}: {valor}")

