print("Bem vindo ao Coletor de Itens!")
mochila = 0
while mochila < 15:
    peso = float(input("Digite o peso do item a ser coletado (em kg): "))
    if peso <= 0:
        print("Peso inválido! Por favor, digite um número positivo.")
        continue
    if peso > 15 - mochila:
        print(
            f"Mochila cheia! Item descartado! Peso final ({mochila}kg).")
        break
    else:
        mochila += peso
        print(
            f"Item coletado! Peso do item: {peso} kg. Capacidade restante da mochila: {15 - mochila} kg.")
