def calcular_frequencia(texto, palavra_alvo):
   
    palavras = texto.lower().split()

    frequencia = palavras.count(palavra_alvo.lower())

    return frequencia


texto_exemplo = input("Digite o texto: ")
palavra_alvo_exemplo = input("Escolha a palavra alvo:")

frequencia_palavra = calcular_frequencia(texto_exemplo, palavra_alvo_exemplo)

print(f"A palavra '{palavra_alvo_exemplo}' aparece {frequencia_palavra} vezes no texto.")
