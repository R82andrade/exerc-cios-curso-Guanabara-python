# Sorteando uma ordem na lista
import random 
n1 = str (input ('Primeiro aluno:'))
n2 = str (input ('Segundo aluno:'))
n3 = str (input ('Teceiro aluno:'))
n4 = str ( input ('Quarto aluno :'))
lista = [ n1, n2, n3, n4]
random.shuffle (lista)
print ('A ordem de apresentação será 1°')
print(lista)