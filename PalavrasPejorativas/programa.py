with open("Python/PalavrasPejorativas/palavras.csv", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Divide o conteúdo em linhas e remove o cabeçalho
linhas = conteudo.strip().split("\n")
lista_palavras_negativas = linhas[1:]  # Pula o cabeçalho

# Remove linhas vazias (caso existam)
lista_palavras_negativas = [palavra for palavra in lista_palavras_negativas if palavra.strip()]

# Ordena a lista
lista_palavras_negativas.sort()

# Mostra a quantidade de palavras pejorativas
print(f"Quantidade de palavras pejorativas: {len(lista_palavras_negativas)}")

# Solicita ao usuário que digite um texto e o divide em palavras
texto = input("Digite um texto: ")
lista_texto = []
lista_texto = texto.split()
print(lista_texto)

# Verifica se as palavras pejorativas estão presentes no texto e conta as ocorrências
for palavra_negativa in lista_palavras_negativas:
    ocorrencias = 0
    for palavra_texto in lista_texto:
        if palavra_negativa == palavra_texto:
            ocorrencias += 1

# Exibe o resultado para cada palavra pejorativa encontrada
if ocorrencias > 0:
    print(f"A palavra '{palavra_negativa}' apareceu {ocorrencias} vezes no texto.")