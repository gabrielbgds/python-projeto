
from math import ceil


def mergesort(lis):  
	lis.sort()
	
Monst = eval(input())
dano = []

for energia, force in Monst:
	
	poder = ceil(energia / 40) - 1
	dano_feito = poder * force
	dano.append(dano_feito)

mergesort(dano)


vitorias = 0
energia = 100
for a in dano:
	
	energia -= a
	if energia > 0:
		vitorias += 1
	else:
		energia = 0
		break
		
        
print(vitorias, energia)