
m2 = float(input('Qual o tamanho da área para ser pintada?: '))

cobertura_por_litro = 3
litros_por_lata = 18
preco_por_lata = 80.00

import math
latas_necessarias = math.ceil(m2 / cobertura_por_litro / litros_por_lata)

preco_total = latas_necessarias * preco_por_lata

print('Você precisará de', latas_necessarias, 'latas de tinta.')
print('O preço total será de R$', preco_total)


