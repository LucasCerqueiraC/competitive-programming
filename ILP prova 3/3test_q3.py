alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
k = int(input())
nome = input()
lista = []
for i in range(len(nome)):
	lista.append(nome[i])
saida = []
q = 0
for i in range(len(lista)):
	for j in range(len(alfabeto)):
		if lista[i] == alfabeto[j]:
			if j + k <= 25:
				saida.append(alfabeto[j + k])
			else:
				q = ((j + k) - 25) - 1
				saida.append(alfabeto[q])
a = ''.join(saida)
print(a)