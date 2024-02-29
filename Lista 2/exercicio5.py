def k_maiores_elementos(lista, k):
    lista_com_indices = [(elemento, indice) for indice, elemento in enumerate(lista)]

    lista_ordenada = sorted(lista_com_indices, key=lambda x: x[0], reverse=True)

    k_maiores = [elemento for elemento, _ in lista_ordenada[:k]]

    return k_maiores

# Exemplo de uso:
lista = input("Digite a lista:")
k = int(input("Digite a quantidade de números que serão retornados:"))
resultado = k_maiores_elementos(lista, k)

print(f"Os {k} maiores elementos na lista são: {resultado}")
