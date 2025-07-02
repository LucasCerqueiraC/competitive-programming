'''
Problema: Luísa precisa sair da escola, visitar o supermercado e a lojinha (em qualquer ordem),
e depois voltar para a escola. Os três locais estão posicionados em uma rua reta, e a distância
entre eles é dada pela diferença de posições. O objetivo é calcular a menor distância total
que Luísa precisa percorrer para fazer todas as visitas e retornar à escola.
'''

# entradas: escola, supermercado e lojinha, respectivamente.
e = int(input())
s = int(input())
l = int(input())
soma = 0          # somente para salvar a variável da distância total percorrida

# na hora acabei não percebendo que independentemente da ordem que ela fosse aos locais, ela sempre andaria da 
# (distancia maxima - distancia minimia) dos locais multiplicado por 2, então acabei escolhendo um caminho mais complicado

# verifica qual local estará mais próximo da escola para decidir a ordem de visita
if s > l:
	# Se o supermercado está depois da lojinha na rua:
    # 1. Vai da escola até a lojinha
    # 2. Depois da lojinha até o supermercado
    # 3. E do supermercado de volta para a escola
	soma = abs(e - l) + abs(l - s) + abs(s-e)
elif l>s:
	# Se a lojinha está depois do supermercado:
    # 1. Vai da escola até o supermercado
    # 2. Depois do supermercado até a lojinha
    # 3. E da lojinha de volta para a escola
	soma = abs(e - s) + abs(s - l) + abs(l - e)

# saida
print(soma)