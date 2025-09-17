lista_notas = []

def cal_media(lista):
    
    if lista:
        soma = sum(lista)
        media = soma / len(lista)
        return media
    
    else:
        print('Não existe notas para calcular.')
        return None

def verificar_int(numero_int):
    try:
        numero_int = int(numero_int)
        return numero_int
    
    except ValueError:
        print ('Opção inserida é invalida.')
        return None

def verificar_float(numero_float_str):
    try:
        numero_float = float(numero_float_str)
        if numero_float >= 0 and numero_float <=10:
            return numero_float
            
        else:
            print('Numero inserido deve ser de 0 a 10.')
            return None
        
    except ValueError:
        print ('Valor inserido é invalido.')
        return None

def listar_notas(lista):
    if lista:
        for i, notas in enumerate(lista):
            print (f'{i+1}) {notas}')
    else:        
        print('Lista está vazia.')

while True:

    menu1_str = input('Digite 1 para adicionar notas\n' \
    'Digite 2 para remover notar \nDigite 3 para verificar as notas inseridas.\n' \
    'Digite 4 para calcular a media e verificar situação do aluno.\n' \
    'Digite 5 para sair.\n')

    menu1 = verificar_int(menu1_str)

    if menu1 is None:
        continue
    
    if menu1 == 1:
        inserir_nota_str = input('Insira a nota:\n')
        inserir_nota = verificar_float(inserir_nota_str)
        
        if inserir_nota is None:
            continue

        lista_notas.append(inserir_nota)

    elif menu1 == 2:
        if lista_notas:
            listar_notas()
            remover_nota_str = input ('Selecione a nota que deseja apagar:\n')
            remover_nota = verificar_int(remover_nota_str)
            
            if remover_nota is None:
                continue
            
            if remover_nota >= 1 and remover_nota <= len(lista_notas):
                del lista_notas[remover_nota-1]
            
            else:
                print('Indice não existe. Verifique novamente.')

        else:
            print('Lista está vazia.')

    elif menu1 == 3:
        listar_notas(lista_notas)

    elif menu1 == 4:
        media = cal_media (lista_notas)

        if media is None:
            continue

        if media >= 7:
            print (f'Media: {media:.2f} \nStatus: Aprovado')
        
        else:
            print (f'Media: {media:.2f} \nStatus: Reprovado')

    elif menu1 == 5:
        print ('Saindo do programa...')
        break

    else:
        print ('Opção inserida é invalida.')