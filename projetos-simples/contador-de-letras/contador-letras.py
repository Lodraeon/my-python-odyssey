frase = 'as informações contidas neste E-mail e nos arquivos anexos são para uso exclusivo do destinatário'.lower() #.lower() será responsavel por deixar todo o texto minusculo, assim conseguindo fazer a comparação de forma igual.

count = 0 #variavel contador, responsavel por encerrar o laço while
letra_mais_vezes = 0 #variavel responsavel por armazenar quantas vezes a letra que mais se repete aparece.
letra_mais_aparece = '' #variavel responsavel por armazenar a letra que aparece mais vezes. No nosso exemplo é a letra "s"


while count < (len(frase)): #enquanto o contador, que começa como 0, for menor que a quantidade de caracteres da frase (len(frase)), o código continuará. Ao final de cada interação, o contador acresenta em 1, encerrando o laço no ultimo indice da frase.
    
    letra_atual = frase[count] #a variavel letra_atual vai armazenar o indice do valor de count da variavel frase. na pratica, isso significa que ele vai começar em 0, que é o valor inicial de count, pegando o primeiro indice da variavel frase. Com cada interação, o valor de count vai subir em um, armazenando o proximo valor do indice da variavel frase.
    
    if letra_atual == ' ': #if responsavel por voltar para o inicio caso haja um espaço.
        count += 1
        continue
    
    letra_quantidade = frase.count(letra_atual) #caso ele passe do if que verifica os espaços, ele determina o valor de uma nova variavel. letra_quantidade armazena a quantidade de vezes que a letra armazenada na variavel letra_atual aparece na frase, com o metodo .count()

    if letra_quantidade > letra_mais_vezes: #se o valor armazenado na variavel anterior for maior que o valor armazenado na variavel letra_mais_vezes, que por padrão se inicia em 0, letra_quantidade recebe o valor de letra_quantidade atual. Além disso, ele armazena a letra que está em letra_atual em letra_mais_aparece, aumentando 1 no contador e reiniciando o laço.
        letra_mais_vezes = letra_quantidade
        letra_mais_aparece = letra_atual
    
    count += 1

print (f'A letra que mais aparece é "{letra_mais_aparece}", aparecendo {letra_mais_vezes} vezes.')