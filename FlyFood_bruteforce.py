import time
from itertools import permutations

# Calculando o tempo
start = time.time()

# Obtendo Matriz através de um arquivo .txt
# arq = str(input('Arquivo: '))
conteudo = open('matrizes\\matriz3.txt', 'r')
texto = conteudo.readlines()

# Construindo a Matriz
matriz = []
for i in range(len(texto)):
    matriz.append(texto[i].split())
conteudo.close()
linhas = int(matriz[0][0])
colunas = int(matriz[0][1])
matriz.remove(matriz[0])

# Coletando os pontos de interesse
pontos = []
dic_F = {}
for x in range(0, linhas):
    for y in range(0, colunas):
        if matriz[x][y] != '0' and matriz[x][y] != 'R':
            pontos.append(matriz[x][y])
        if matriz[x][y] != '0':
            dic_F[matriz[x][y]] = (x, y)

# Todas as permutações nos pontos de interesse
listaPerm = list(permutations(pontos))

# Cálculo distâncias
# Variávies para cálculo de melhor rota
menorRota = 0
menorCaminho = []

for p in listaPerm:
    rts = r = 0
    p = list(p)

    # Acrescentando R no começo e no final das rotas
    p.append('R')
    p.insert(0, 'R')

    # Calculando as distâncias
    while r < len(p) - 1:
        dis = abs(dic_F[p[r]][0] - dic_F[p[r + 1]][0]) + abs(dic_F[p[r]][1] - dic_F[p[r + 1]][1])
        rts += dis
        r += 1

    # print(rts, p)

    # Calculo de melhor rota
    if rts < menorRota or menorRota == 0:
        menorRota = rts
        menorCaminho = ' → '.join(p)

# Resultado
print(f'O menor percurso foi de {menorRota} dronômetros, com a rota: {menorCaminho}')

end = time.time()

delta = round(end - start, 3)
print(f'Código finalizado em {delta} segundos')
