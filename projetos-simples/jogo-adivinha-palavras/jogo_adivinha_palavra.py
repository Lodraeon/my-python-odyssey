palavra_secreta = 'são paulo'

palavra_formatada = ''

tentativas = 0

for letra in palavra_secreta:
    if letra == ' ':
        palavra_formatada += ' '
        tentativas -= 1
    else:
        palavra_formatada += '*' 


print ('Bem vindo ao jogo da adivinhação, onde você precisa acertar a palavra que eu estou pensando! ')

print ('Você vai digitar uma letra por vez. Caso a letra que você digitou esteja na palavra secreta,')
print ('ela será exibida!')

print('Tente acertar a palavra com o menor de tentativas possiveis! ')

print (f'A palavra secreta contem o seguinte numero de caracteres: {palavra_formatada}')

while True:
    palavra_temporaria = ''
    letra_tentativa = input('Insira a letra: ').lower()

    if letra_tentativa.isalpha():
            
        if len(letra_tentativa) > 1:
            print ('Insira apenas uma letra!')
        
        else:

            for letra in palavra_secreta:
                if letra_tentativa == letra:
                    palavra_temporaria += letra_tentativa

                elif letra in palavra_formatada:
                    palavra_temporaria += letra

                else:
                    palavra_temporaria += '*'

            palavra_formatada = palavra_temporaria
            tentativas += 1
            if palavra_formatada == palavra_secreta:
                print ('Parabens, você acertou!')
                if tentativas <= (len(palavra_secreta)):
                    print (f'A palavra secreta é {palavra_formatada}. Você acertou corretamente todas as letras de uma vez só! \nBrilhante!')
                    break
                else:
                    print (f'A palavra secreta é {palavra_formatada}. Você tentou {tentativas} vezes! \nContinue tentando melhorar seu recorde!')
                    break

            print (f'Palavra: {palavra_formatada}')           

    else:
        print ('Insira apenas letras!')