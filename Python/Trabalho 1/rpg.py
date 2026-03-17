print("Bem vindo ao RPG!")
hp_player = 100
hp_monster = 100
turno = 1
while hp_player > 0 and hp_monster > 0:
    print(f"Turno {turno}:")
    ataque_player = int(input("Digite o valor do seu ataque (1-20): "))
    if ataque_player < 1 or ataque_player > 20:
        print("Valor de ataque inválido! Por favor, digite um número entre 1 e 20.")
        continue
    ataque_monster = int(input("Digite o valor do ataque do monstro (1-20): "))
    if ataque_monster < 1 or ataque_monster > 20:
        print("Valor de ataque inválido! Por favor, digite um número entre 1 e 20.")
        continue
    hp_monster -= ataque_player
    hp_player -= ataque_monster
    print(
        f"Você causou {ataque_player} de dano ao monstro. HP do monstro: {hp_monster}")
    print(
        f"O monstro causou {ataque_monster} de dano a você. Seu HP: {hp_player}")
    if hp_player <= 0:
        print("Você foi derrotado pelo monstro!")
    elif hp_monster <= 0:
        print("Parabéns! Você derrotou o monstro!")
    turno += 1
