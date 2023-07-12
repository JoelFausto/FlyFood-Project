import time

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

pontos.insert(0, 'R')


# Função para Cálculo de distâncias
def calc_distancia(x1, y1, x2, y2):
    distancia = abs(abs((x1 - y1)) + abs((x2 - y2)))
    return distancia


# Função Algoritmo Vizinho mais próximo
def A_Vizinho(lista, dic):
    rota = ['R']
    soma = 0
    ponto = None

    for p in range(len(lista) - 1):
        c = menor = 0
        while c < len(lista) - 1:
            d = calc_distancia(dic[lista[0]][0], dic[lista[c + 1]][0], dic[lista[0]][1], dic[lista[c + 1]][1])
            # print(lista[0], lista[c + 1], d)
            c += 1
            if d < menor or menor == 0:
                menor = d
                ponto = pontos[c]
        soma += menor
        lista.remove(rota[-1])
        lista.remove(ponto)
        lista.insert(0, ponto)
        rota.append(ponto)
        # print(menor, ponto)

    # Quando já tiver percorrido todos os pontos, ele deve voltar ao ponto 'R':
    lista.append('R')
    d = calc_distancia(dic[lista[0]][0], dic[lista[1]][0], dic[lista[0]][1], dic[lista[1]][1])
    soma += d
    rota.append('R')
    rota = ' → '.join(rota)

    return f'O menor percurso encontrado foi de {soma} dronômetros, com a rota: {rota}'


print(A_Vizinho(pontos, dic_F))

end = time.time()

delta = round(end - start, 3)
print(f'Código finalizado em {delta} segundos')
