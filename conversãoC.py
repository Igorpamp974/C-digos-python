def celcius_para_fahrenheit(celsius):
      fahrenheit = (celsius * 1.8) +32
      return fahrenheit

temperatura_em_celsius = float(input('Qual a temperatura que deseja para a conversão: ?'))
temperatura_em_fahrenheit = celcius_para_fahrenheit(temperatura_em_celsius)

print(f'A temperatura convertida é: {temperatura_em_fahrenheit:.2f}')
