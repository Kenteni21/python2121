numero = int(input('Digite um numero inteiro: '))

if (numero % 2) == 0:
    numero += 5
    print('Par')
else:
    numero += 8
    print('Impar')

print(numero)
