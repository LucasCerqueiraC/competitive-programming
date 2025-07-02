'''
Problema: Gerar um gráfico de barras vertical com N colunas representando a popularidade de brinquedos, usando
apenas 0 e 1. A altura H do gráfico é igual à maior popularidade, e cada coluna tem Xi números 1 na base e H - Xi
zeros no topo.
'''
#entradas
N = int(input())    # colunas da matriz
lista = list(map(int, input().split()))
altura = max(lista)   # linhas da matriz

matriz = [[0] * N for _ in range(altura)] #matriz inicial somente com 0s

#define até onde vai os 1s nas colunas começando por baixo
for j in range(N):
    votos = lista[j]
    for i in range(altura - votos, altura):
        matriz[i][j] = 1

#saída
for linha in matriz:
    print(*linha)