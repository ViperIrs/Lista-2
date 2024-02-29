def menor_string(lista_de_strings):
    if not lista_de_strings:
        return None  # Retorna None se a lista estiver vazia

    menor = lista_de_strings[0]

    for string in lista_de_strings[1:]:
        if len(string) < len(menor):
            menor = string

    return menor

# Exemplo de uso:
lista_de_strings = ["banana", "maçã", "laranja", "uva", "abacaxi"]

menor = menor_string(lista_de_strings)

print(f"A menor string na lista é: {menor}")
