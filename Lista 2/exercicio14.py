import csv

def ler_arquivo_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            
            # Lê e imprime cada linha do arquivo CSV
            for linha in leitor_csv:
                print(linha)
                
    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

# Exemplo de uso:
caminho_do_arquivo_csv = "caminho/do/arquivo.csv"

ler_arquivo_csv(caminho_do_arquivo_csv)
