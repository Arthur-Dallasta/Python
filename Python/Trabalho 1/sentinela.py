print("Bem vindo ao Monitor de Inundação Sentinela!")
nivel = 0
while nivel >= 0:
    nivel = float(input("Digite o nível de inundação (em metros, ou um número negativo para sair): "))
    if nivel < 0:
        print("Encerrando o Monitor de Inundação Sentinela. Fique seguro!")
    elif nivel < 3:
        print("Nível de inundação normal. Risco mínimo.")
    elif nivel >= 3 and nivel <= 5:
        print("Nível de inundação moderado. Fique atento.")
    else:
        print("Nível de inundação alto! Evacuação imediata!")