n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
meio = (n1 + n2 + n3 ) - maior - menor

print('Os valores em ordem decrescente são:', maior,meio,menor)