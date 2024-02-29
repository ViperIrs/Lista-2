import os

def consolidar_arquivos(diretorio_origem, arquivo_destino):
    try:
        with open(arquivo_destino, 'w', encoding='utf-8') as arquivo_final:
            for nome_arquivo in os.listdir(diretorio_origem):
                caminho_arquivo = os.path.join(diretorio_origem, nome_arquivo)

                if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith('.txt'):
                    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_atual:
                        conteudo_arquivo_atual = arquivo_atual.read()
                        arquivo_final.write(conteudo_arquivo_atual)
                        arquivo_final.write('\n')  

        print(f"Consolidação concluída. Arquivo consolidado salvo em: {arquivo_destino}")
    except Exception as e:
        print(f"Erro ao consolidar os arquivos: {e}")


diretorio_de_origem = "caminho/do/diretorio"
arquivo_destino = "caminho/do/arquivo/consolidado.txt"

consolidar_arquivos(diretorio_de_origem, arquivo_destino)
