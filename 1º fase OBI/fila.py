'''
Problema: Dada a altura de N alunos dispostos em fila única, identificar quantos alunos o professor não consegue
enxergar, pois estão bloqueados por alunos mais altos ou de altura igual que estão à frente (mais perto do professor).
'''

# entradas
n = int(input())
lista = list(map( int, input().split()))  #altura dos alunos em ordem da fila

i = n - 1  # índice para percorrer os alunos de trás para frente
soma = 0   # contador para alunos invisiveis
alto = 0   # guarda a maior altura já vista

while i >= 0:
    if lista[i] > alto:
          alto = lista[i]  # atualiza a maior altura
    else:                  # alunos bloqueados por um mais alto ou mesma altura à sua frente
         soma += 1
    i -= 1                 # vai para o aluno de trás

# saída: quantidade de alunos que o professor não consegue enxergar
print(soma)