import os
os.system('cls')

# try:
#     n = int(input('Digite um número: '))
# except:
#     print('Erro')


try:
    n = (input('Digite uma letra: '))[0]
except (ValueError,KeyboardInterrupt) as e :
    print(f'Erro {e}')
else:
    print(f'Você informou {n}')

    


# try:
#     n = int(input('Digite um número: '))
# except ValueError as e :
#     print(f'{e}')
# except KeyboardInterrupt as e :
#     print(f'\n Operação cancelada pelo usuario')
    




# try: 
#     txt = int(input("Informe o nome: "))
# except IndexError as e : 
#     print(f'Precisa digitar algo{e}: ')
# else:
#     print(f'Acertou')
# finally:
#     n = txt + 50

#     print(f'A soma é {n}')