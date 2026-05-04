def ler_arquivo(caminho):
    jogadores = []
    arquivo = open(caminho, "r", encoding="utf-8")
    for linha in arquivo:
        linha = linha.strip()
        if linha == "":
            continue
        dados = linha.split(";")
        jogador = {
            "nome": dados[0],
            "classe": dados[1],
            "kills": int(dados[2]),
            "deaths": int(dados[3]),
            "dano": int(dados[4])
        }
        jogadores.append(jogador)
    arquivo.close()
    return jogadores


def calcular_kda(kills, deaths):
    if deaths == 0:
        return float(kills)
    return kills / deaths


def filtrar_por_classe(jogadores, classe):
    resultado = []
    for j in jogadores:
        if j["classe"] == classe:
            resultado.append(j)
    return resultado


def gerar_relatorio(jogadores):
    maior_dano = jogadores[0]
    for j in jogadores:
        if j["dano"] > maior_dano["dano"]:
            maior_dano = j

    print("=== RELATÓRIO DE PERFORMANCE ===\n")
    print(f"Maior dano causado: {maior_dano['nome']} ({maior_dano['dano']} de dano)")

    total_kills = 0
    for j in jogadores:
        total_kills += j["kills"]
    media_kills = total_kills / len(jogadores)
    print(f"Média de kills da partida: {media_kills:.2f}")

    print("\nJogadores com KDA superior a 2.0:")
    destaque_encontrado = False
    for j in jogadores:
        kda = calcular_kda(j["kills"], j["deaths"])
        if kda > 2.0:
            print(f"  - {j['nome'].upper()} (KDA: {kda:.2f})")
            destaque_encontrado = True
    if not destaque_encontrado:
        print("  Nenhum jogador atingiu KDA superior a 2.0.")

    print("\n--- Jogadores por Classe ---")
    classes = []
    for j in jogadores:
        if j["classe"] not in classes:
            classes.append(j["classe"])
    classes.sort()
    for classe in classes:
        membros = filtrar_por_classe(jogadores, classe)
        nomes = ""
        for i in range(len(membros)):
            if i == 0:
                nomes = membros[i]["nome"]
            else:
                nomes = nomes + ", " + membros[i]["nome"]
        print(f"{classe}: {nomes}")


jogadores = ler_arquivo("partida.txt")
gerar_relatorio(jogadores)
