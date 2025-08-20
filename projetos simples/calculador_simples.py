print ('Bem vindo a calculadora!')

while True: #laço responsavel pela estrutura do menu.

    escolha1 = input('Digite 1 para continuar ou 2 para sair: ') # o numero digitado pelo usuario vai automaticamente para o try, que tentará converter o valor inserido em uma variavel do tipo inteiro. Tentar converter para um numero inteiro é a melhor pratica para esse menu, pois apenas 1 e 2 são opções validas.

    try:
        menu1 = int(escolha1) #python tentará converter a variavel (escolha1) em um valor de tipo inteiro. Caso ocorra algum erro, como o valor ser uma string, ele vai direto para o except, informando o usuario que o caracter inserido é invalido e retornando para o começo do laço.

        if menu1 == 1: #se o valor inserido pelo usuario for igual a 1, esperado para continuar o programa, o python segue com a leitura do código. Abaixo do if, um elif capta se o usuario inseriu 2, esperado caso o usuario queira encerrar o programa, exibindo uma mensagem e em seguida um break que encerrará o loop e o código.

            numero_final = 0 #variavel responsavel por armazenar o valor final da conta que será feita pelo usuario. Como está sendo definida depois do menu, ela sempre retornará para o valor 0, ideal para continuar com novas operações.
            
            while True: #laço responsavel por validar se o numero inserido pelo usuario para a operação é valido. Após o usuario inserior o primeiro numero, o código tentará, através do "try", converter o valor para um tipo flutuante. Caso consiga, será armazenado como um numero flutuante e o break quebrará o laço. Caso caia no except, ou seja, sejá uma string, ele exibirá uma mensagemde erro e voltará para o inicio do laço. 
                numero1 = input ('Digite o primeiro numero: ')
                try:
                    numero1 = float(numero1)
                    break
                except ValueError:
                    print ('Caracter detectado! Insira apenas numero inteiros ou decimais! ')


            while True: #mesma logica do laço acima. A unica diferença que vale a pena ser citada é que utilizamos um if-elif-else para capturar erros ao inves do try, pelo dado ser do tipo string. O if poderia ser simplificado, criando uma nova variavel como "operadores_validos = '+-/*'" e utilizando o if operador not in operadores_validos para exibir uma mensagem de erro. Além disso, utilizei a função len(operador) para caso o numero de operadores inseridos seja maior que 1, uma mensagem de erro seja exibida.
                operador = input ('Digite a operação que quer fazer\n' \
                '"+" para adição - "-" para subtração - "*" para multiplicação - "/" para divisão: \n')
                if operador == '+' or operador == '-' or operador == '*' or operador == '/':
                        break
                elif len(operador) > 1:
                    print ('Digite apenas um operador.')
                else:
                    print('Operador logico invalido.')
            

            while True: #mesma logica do while numero1
                numero2 = input ('Digite o segundo numero: ')
                try:
                    numero2 = float(numero2)
                    break
                except ValueError:
                    print ('Caracter detectado! Insira apenas numero inteiros ou decimais! ')

            
            #estrura if-elif-else simples para realizar as contas, utilizando f strings para exibir o valor das variaveis. Vale destacar o :g utilizado ao final do valor da variavel numero_final, para exibir casas decimais quando for flutuante e sem casas decimais quando for numero inteiro.

            if operador == '+':
                numero_final = numero1 + numero2
                print(f'{numero1} + {numero2} = {numero_final:g}')

            elif operador == '-':
                numero_final = numero1 - numero2
                print(f'{numero1} - {numero2} = {numero_final:g}')

            elif operador == '*':
                numero_final = numero1 * numero2
                print(f'{numero1} * {numero2} = {numero_final:g}')

            elif operador == '/': 
                if numero2 == 0: #um ponto de interesse é o if inserido dentro do elif da operação de divisão. Como é impossivel um numero ser dividido por 0, o if pega o segundo numero (divisor) e verifica se ele é igual a 0. Se for, ele exibe uma mensagem de erro, voltando para o inicio do programa.
                    print('Erro logico! Impossivel dividir um numero por zero.')
                else:
                    numero_final = numero1 / numero2
                    print(f'{numero1} / {numero2} = {numero_final:g}')


        elif menu1 == 2: #elif responsavel por encerrar o programa com um break.
            print ('Encerrando calculadora...')
            break

        else: #mensagem de erro exibida caso o usuario digite um numero inteiro que não seja 1 ou 2.
            print ('Numero inserido é invalido!')
    
    except ValueError: #erro referente ao menu1, caso o usuario digite um numero flutuante ou string.
        print ('Caracter ou numero decimal detectado! Use apenas numeros inteiros!')