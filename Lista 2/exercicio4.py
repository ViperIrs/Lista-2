def contar_ocorrencias(frase, palavra_alvo):
    palavras = frase.split()
    contador = 0

    for palavra in palavras:
        if palavra == palavra_alvo:
            contador += 1

    return contador

frase_exemplo = input("Digite uma frase:")
palavra_alvo = input("Digite a palavra chave:")
num_ocorrencias = contar_ocorrencias(frase_exemplo.lower(), palavra_alvo.lower())

print(f"A palavra '{palavra_alvo}' ocorre {num_ocorrencias} vezes na frase.")
