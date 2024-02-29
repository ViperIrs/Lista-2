import json

def ler_arquivo_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json
    except FileNotFoundError:
        print(f"Arquivo JSON não encontrado: {caminho_arquivo}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {e}")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {e}")
        return None

# Exemplo de uso:
caminho_do_arquivo_json = "caminho/do/arquivo.json"

dados_do_json = ler_arquivo_json(caminho_do_arquivo_json)

if dados_do_json:
    print("Conteúdo do arquivo JSON:")
    print(json.dumps(dados_do_json, indent=2))  # Imprime o JSON formatado
