def entrada_dados(nome_controle, campos):
    dados = {}

    print(f"--- {nome_controle}:")
    for campo in campos:
<<<<<<< HEAD
        try:
            dados[campo] = int(input(f"{campo}: "))
        except ValueError:
            print("Digite um número valido")
=======
        dados[campo] = input(f"{campo}: ")

>>>>>>> 9b7155a52424ad28fc58b2e9234585ad77dd1994

    print(f"---- Resumo de {nome_controle}:")
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")

<<<<<<< HEAD
       
    total = sum(dados.values()) 
    print(f"Valor total: {total}")

    print("Vendas no salao:", dados.get("Vendas no salao"),  "\nComissão:", dados.get("Comissão") )

campos_recebimento_diario = ["Despesas", "Fita (Valor Total)", "Comissão", "Voucher", "Vendas no salao",  "Dif (Soma dos pagamentos - Dinheiro e Pendura)", "Soma do Relatorio de vendas"]
campos_controle_contabil = ["Fornecedor", "Valor", "Número da nota", "Forma de Pagamento", "Data de emissão"]

def main():
    options = int(input("Digite 1 para entar com dados contabeis, Digite 2 para entrar com o recebimento diario"))
    if options == 1:
        dados_contabil = entrada_dados("Controle Contabil", campos_controle_contabil)
    elif options == 2:
        dados_recebimento = entrada_dados("Controle de Recebimento Diario", campos_recebimento_diario)


if __name__ == "__main__":
    main()
=======

campos_recebimento_diario = ["Despesas", "Fita (Valor Total)", "Comissão", "Voucher"]
dados_recebimento = entrada_dados("Controle de Recebimento Diario", campos_recebimento_diario)

campos_controle_contabil = ["Fornecedor", "Valor", "Número da nota", "Forma de Pagamento", "Data de emissão"]
dados_contabil = entrada_dados("Controle Contabil", campos_controle_contabil)




>>>>>>> 9b7155a52424ad28fc58b2e9234585ad77dd1994
