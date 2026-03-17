print("Bem vindo ao Monitor de Média Temperatura!")
dias = int(input("Digite o número de dias para calcular a média: "))
if dias <= 0:
    print("Número de dias inválido! Por favor, digite um número positivo.")
else:
    soma = 0
    i = 0
    while i < dias:
        temperatura = float(input(f"Digite a temperatura do dia {i+1}: "))
        soma += temperatura
        i += 1
    media = soma / dias
    print(f"A média de temperatura dos {dias} dias é: {media:.2f}°C")
    if media > 25:
        print("Media acima do esperado!")
    elif media <= 25:
        print("Media dentro da normalidade!")

