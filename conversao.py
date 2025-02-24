def fahreinheit_para_celsius(fahreinheit):
    celsius = 5 *((fahreinheit - 32)/9)
    return celsius

temperatura_em_fahreinheit = float(input('Qual a temperatura em graus fahrenheit?: '))

temperatura_celsius = fahreinheit_para_celsius(temperatura_em_fahreinheit)

print(f'a temperatura convertida é {temperatura_celsius:.2f}')