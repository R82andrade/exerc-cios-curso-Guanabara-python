
# Procurando uma string dentro de outra
nome = str (input('Qual é seu nome completo?')).strip ()
print ('Seu nome tem Silva? {}'.format ('Silva' in nome.lower()))