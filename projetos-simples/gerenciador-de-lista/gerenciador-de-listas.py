import os

lista = []

while True:
    print('Selecione uma opção: ')
    menu1 = input('1 para inserir um novo item / 2 para apagar um item da lista / 3 para listar\n')
    
    try:
        menu1 = int(menu1)

        if menu1 == 1:
            item = input('Insira o nome do item que deseja inserir:\n')
            caracteres_invalidos = False
            for caracteres in item:
                if not caracteres.isalpha() and not caracteres.isspace():
                    caracteres_invalidos = True
                    break
            if caracteres_invalidos == True:
                os.system ('cls')
                print ('Numeros detectados. Insira apenas letras e espaços.')
            else:
                if len(item) > 15:
                    os.system ('cls')
                    print ('Nome muito grande. Insira um item com menos de 15 letras.')
                else:
                    lista.append(item)
                    os.system ('cls')
                            
            

        elif menu1 == 2:
            os.system ('cls')
            if len(lista) == 0:
                print('Não existem itens para serem apagados')
            else:
                item_apagar = input('Digite o numero do item que quer apagar:\n')
                try:
                    item_apagar = int(item_apagar)
                    del lista[item_apagar]
                    os.system ('cls')
                except ValueError:
                    os.system ('cls')
                    print('Insira apenas numeros inteiros.')
                except IndexError:
                    os.system ('cls')
                    print ('Numero de item inexistente, confirme o numero correto na lista.')
                except:
                    os.system ('cls')
                    print ('Você não deveria ver esse erro. Entre em contato com o administrador. ')


        elif menu1 == 3:
            if len(lista) == 0:
                os.system ('cls')
                print ('Lista vazia.')
            else:    
                os.system ('cls')
                print('Lista:')
                for indice, nomes in enumerate(lista):
                    print (indice, nomes)

        else:
            os.system ('cls')
            print ('Digite as opções de 1 a 3.')

    
    except:
        os.system ('cls')
        print('Opção inserida invalida.')