import csv

def somar_vendas_por_vendedor(caminho_arquivo):
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

            return vendas_por_vendedor

    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None


caminho_do_arquivo_csv = "dados_vendas.csv"

soma_vendas_por_vendedor = somar_vendas_por_vendedor(caminho_do_arquivo_csv)

if soma_vendas_por_vendedor:
    print("Soma de vendas por vendedor:")
    for vendedor, total_vendas in soma_vendas_por_vendedor.items():
        print(f"{vendedor}: {total_vendas}")
