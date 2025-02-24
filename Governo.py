
ganho_por_hora = float(input('Quanto você ganha por hora?: '))
horas_trabalhadas_mes = float(input('Qual seu número de horas trabalhadas por mes?: '))

A = ganho_por_hora + horas_trabalhadas_mes
B = A * 0.11
C = A * 0.08
D = A * 0.05
E = A - (B + C + D)

print('+ Sálario bruto : R$ {:.2f}'.format(A))
print('- IR (11%) : R$ {:.2f}'.format(B))
print('- INSS (8%) : R$ {:.2f}'.format(C))
print('- SINDICATO (5%) : R$ {:.2f}'.format(D))
print('= SALARIO LIQUIDO : R$ {:.2f}'.format(E))