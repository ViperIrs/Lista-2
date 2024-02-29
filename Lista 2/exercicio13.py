def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        return f"Arquivo não encontrado: {caminho_arquivo}"
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

caminho_do_arquivo = "caminho/do/arquivo.txt"

conteudo_arquivo = ler_arquivo(caminho_do_arquivo)

if conteudo_arquivo:
    print(f"Conteúdo do arquivo:\n{conteudo_arquivo}")
else:
    print("Erro ao ler o arquivo.")
