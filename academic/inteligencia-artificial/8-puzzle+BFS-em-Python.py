# Estado: lista de listas, 0 = vazio

estado_inicial = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

estado_objetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def objetivo(estado):
    return estado == estado_objetivo


# Cada função localiza o vazio e tenta mover a peça vizinha.
# Retorna None se o movimento for inválido (borda).

def mover_cima(tab):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0 and i > 0:
                n = [r[:] for r in tab]
                n[i][j], n[i - 1][j] = n[i - 1][j], n[i][j]
                return n
    return None


def mover_baixo(tab):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0 and i < 2:
                n = [r[:] for r in tab]
                n[i][j], n[i + 1][j] = n[i + 1][j], n[i][j]
                return n
    return None


def mover_esquerda(tab):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0 and j > 0:
                n = [r[:] for r in tab]
                n[i][j], n[i][j - 1] = n[i][j - 1], n[i][j]
                return n
    return None


def mover_direita(tab):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0 and j < 2:
                n = [r[:] for r in tab]
                n[i][j], n[i][j + 1] = n[i][j + 1], n[i][j]
                return n
    return None


from collections import deque

operadores = [
    mover_cima,
    mover_baixo,
    mover_esquerda,
    mover_direita
]


def expandir(estado):
    vizinhos = []

    for op in operadores:
        resultado = op(estado)

        if resultado is not None:
            vizinhos.append(resultado)

    return vizinhos


def bfs(inicial):
    fila = deque([[inicial]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        estado = caminho[-1]

        if objetivo(estado):
            return caminho

        chave = str(estado)

        if chave in visitados:
            continue

        visitados.add(chave)

        for viz in expandir(estado):
            fila.append(caminho + [viz])

    return None


solucao = bfs(estado_inicial)

if solucao:
    print(f"Solução em {len(solucao) - 1} movimentos")

    for i, passo in enumerate(solucao):
        print(f"\nPasso {i}:")

        for linha in passo:
            print(linha)
else:
    print("Sem solução encontrada")


# Mantém a janela aberta quando o programa é iniciado com dois cliques.
input("\nPressione Enter para fechar...")
