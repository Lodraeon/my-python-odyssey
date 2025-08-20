#preciso achar qual letra aparece mais vezes na frase.

frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

letra_mais_qtd = ''
quantidade_maior = 0

count = 0

while count <= (len(frase)):

    count += 1
    print (frase.count('o'))