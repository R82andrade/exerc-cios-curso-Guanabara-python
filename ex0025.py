# Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase')).upper().strip()
print('A letra aparece {} vezes na frase'.format (frase.count('A')))
print ('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print ('A ultima letra A apareceu na posição {}'.format(frase.find('A')+1))