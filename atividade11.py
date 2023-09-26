def calcularvalor(preco, codigo_condicao_pagamento):
    if codigo_condicao_pagamento == 1:
        return preco * 0.9 
    elif codigo_condicao_pagamento == 2:
        return preco * 0.85 
    elif codigo_condicao_pagamento == 3:
        return preco
    elif codigo_condicao_pagamento == 4:
        return preco * 1.1  
    else:
        return "Condição de pagamento inválida"

preco = float(input("Digite o preço normal de etiqueta do produto: "))
codigo_condicao_pagamento = int(input("Digite o código da condição de pagamento 1 - À vista em dinheiro ou cheque: 2 - À vista no cartão de crédito: 3 - Em duas vezes: 4 - Em duas vezes, maior prazo:"))

valorpagar = calcularvalor(preco, codigo_condicao_pagamento)
print("Valor a pagar:", valorpagar)