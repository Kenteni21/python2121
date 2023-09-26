a = bool(input('Digite o valor lógico de a: '))
b = bool(input('Digite o valor lógico de b: '))

a = a == 'True'
b = b == 'True'

if a and b:
    print('Ambos os valores são verdadeiros')
else:
    print('Ambos os valores não são verdadeiros')