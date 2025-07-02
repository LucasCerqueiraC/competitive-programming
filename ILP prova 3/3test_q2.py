n = int(input())
lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
lista3 = list(map(int, input().split()))
i = 0
soma = 0
while i <= n - 1:
	s = lista1[i] + lista2[i]
	if s == lista3[i]:
		soma += 1
	i += 1
if soma == n:
	print("OK")
else:
	print('NOPE :( ')