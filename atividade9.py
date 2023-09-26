h = float(input('Indique sua altura: '))
sx = (input('Indique seu sexo (F) ou (M): '))

def calcular_peso_ideal(h, sx):
    if sx == 'M':
        return (72.7 * h) - 58
    elif sx == 'F':
        return (62.1 * h) - 44.7
    else:
        return "Sexo inválido. Por favor, insira 'M ou 'F'."

print("Seu peso ideal é: ", calcular_peso_ideal(h, sx))