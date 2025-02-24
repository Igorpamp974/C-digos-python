peso = float(input('Digite o peso dos peixes por kg: '))
limite = 50
multa_por_quilo = 4.00

excesso = max(0, peso - limite)
multa = excesso * multa_por_quilo

print('===== Resultado =====')
print(f'Peso informado: {peso:.2f} kg')
print(f'Excesso: {excesso:.2f} kg')
print(f'Multa a pagar: R$ {multa:.2f}')