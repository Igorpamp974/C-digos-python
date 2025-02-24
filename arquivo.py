tamanho_arquivo = float(input('Qual o tamanho do arquivo para download?: '))
velocidade_link = float(input('Qual a velocidade do link de internet?: '))

velocidade_link_MBps = velocidade_link * 0.125

tempo_em_segundos = tamanho_arquivo / velocidade_link_MBps

tempo_em_minutos = tempo_em_segundos / 60

print(f'O tempo aproximado de download é de {tempo_em_minutos:.2f}')