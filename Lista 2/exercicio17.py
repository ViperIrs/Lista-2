import csv

def mes_com_mais_vendas(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            
            vendas_por_mes = {}

            for linha in leitor_csv:
                mes = linha['Mês']
                valor = int(linha['Valor'])
                
                if mes in vendas_por_mes:
                    vendas_por_mes[mes] += valor
                else:
                    vendas_por_mes[mes] = valor

            mes_mais_vendas = max(vendas_por_mes, key=vendas_por_mes.get)

            return mes_mais_vendas

    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None


caminho_do_arquivo_csv = "caminho/do/arquivo.csv"

mes_com_maior_venda = mes_com_mais_vendas(caminho_do_arquivo_csv)

if mes_com_maior_venda:
    print(f"O mês com mais vendas é: {mes_com_maior_venda}")
