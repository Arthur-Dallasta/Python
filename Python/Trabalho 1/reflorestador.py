print("Bem vindo ao Reflorestador!")
meta = int(input("Digite a sua meta de Biomassa (em unidades): "))
arvores_plantadas = 0
while arvores_plantadas < meta:
    novas_arvores = int(
        input("Digite o número de árvores que deseja plantar: "))
    arvores_plantadas += novas_arvores
    if arvores_plantadas >= meta:
        print("Parabéns! Você atingiu sua meta de Biomassa!")
    else:
        print(
            f"Você ainda precisa plantar {meta - arvores_plantadas} árvores para atingir sua meta.")
