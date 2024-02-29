import csv

def encontrar_vendedores_mais_e_menos_vendas(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            
            vendas_por_vendedor = {}

            for linha in leitor_csv:
                vendedor = linha['Vendedor']
                valor_venda = int(linha['Valor'])
                
                if vendedor in vendas_por_vendedor:
                    vendas_por_vendedor[vendedor] += valor_venda
                else:
                    vendas_por_vendedor[vendedor] = valor_venda

            vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)

            vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)

            return vendedor_mais_vendeu, vendedor_menos_vendeu

    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {caminho_arquivo}")
        return None, None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None, None

caminho_do_arquivo_csv = "dados_vendas.csv"

mais_vendeu, menos_vendeu = encontrar_vendedores_mais_e_menos_vendas(caminho_do_arquivo_csv)

if mais_vendeu and menos_vendeu:
    print(f"Vendedor que mais vendeu: {mais_vendeu}")
    print(f"Vendedor que menos vendeu: {menos_vendeu}")
