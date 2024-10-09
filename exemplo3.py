import os
os.system('cls')

lista = [1,2,3,4,5]

try:
    resp = int(input('Informe a posição que você quer acessar: '))
    print(lista[resp])
except ValueError as e:
    print( f'{e} Digite apenas números inteiros')
except IndexError as e :
    print(f'{e}')