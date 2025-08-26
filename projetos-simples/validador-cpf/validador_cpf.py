import os

while True:
    menu1 = input('Digite 1 para continuar ou 2 para sair:\n')
    os.system ('cls')
    try:
        menu1 = int(menu1)
        if menu1 == 1:

            cpf = input('Digite o numero do seu CPF:\n')
            os.system ('cls')
            cpf_tratado = ''
            numeros_iguais = 0
            verificador_letras = False

            for digitos in cpf:
                if digitos == '-' or digitos == '.':
                    continue

                elif digitos.isdigit():
                    cpf_tratado += digitos
                
                else:
                    verificador_letras = True
            
            if verificador_letras:
                print('Letras detectadas, tente novamente.')
                continue

            caracter_repetido = cpf_tratado [0] * len(cpf_tratado)
            if cpf_tratado == caracter_repetido:
                print('Você inseriu onze numeros iguais, esse é um formato invalido para CPF.')
                continue

            if len(cpf_tratado) == 11:

                cpf_novo = cpf_tratado [:9]
                multiplicador = 10
                soma_digitos_multiplicados = 0
                cpf_mais_primeiro_digito = cpf_novo

                for numeros in cpf_novo:
                    numeros = int(numeros) * multiplicador
                    soma_digitos_multiplicados += numeros
                    multiplicador -= 1
                
                resto_divisao = (soma_digitos_multiplicados * 10) % 11
                resultado_primeiro_digito = 0 if resto_divisao > 9 else resto_divisao

                multiplicador = 11
                cpf_mais_primeiro_digito += str(resultado_primeiro_digito)
                soma_digitos_multiplicados = 0

                for numeros in cpf_mais_primeiro_digito:
                    numeros = int(numeros) * multiplicador
                    soma_digitos_multiplicados += numeros
                    multiplicador -= 1

                resto_divisao = (soma_digitos_multiplicados * 10) % 11
                resultado_segundo_digito = 0 if resto_divisao > 9 else resto_divisao

                cpf_algoritmo = f'{cpf_novo}{resultado_primeiro_digito}{resultado_segundo_digito}'

                if cpf_algoritmo == cpf_tratado or cpf_algoritmo == cpf:
                    print(f'O cpf {cpf} é valido.')
                else:
                    print(f'O cpf {cpf} é invalido.')

            else:
                print('Tamanho do CPF invalido.')

        elif menu1 == 2:
            print('Saindo do programa...')
            break

        else:
            print('Opção invalida.')

    except ValueError:
        print ('Caracter digitado invalido.')