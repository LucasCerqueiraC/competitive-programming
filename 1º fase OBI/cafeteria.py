'''
Problema: Felipe precisa preparar uma bebida com café espresso e leite para um cliente, 
considerando as preferências de volume mínimo (minL) e máximo (maxL) de leite, a capacidade (cap) da xícara 
e o volume fixo (dose) de cada dose de café espresso. O objetivo é determinar se existe um número de doses 
inteiras de café (múltiplos da dose) que, ao completar com leite, respeite a faixa de leite desejada pelo cliente.
'''
# entradas
minl = int(input())
maxl = int(input())
cap = int(input())
dose = int(input())

# calcula a quantidade de leite que sobra após usar essas doses de café e o volume mínimo de leite
leite = minl + ((cap - minl) % dose)

#saida: fala se não é possível ("N") ou que é possível satisfazer as condições do cliente ("S")
if leite > maxl:   # Verifica se a quantidade calculada de leite ultrapassa o máximo permitido pelo cliente
    print("N")
else:
    print("S")