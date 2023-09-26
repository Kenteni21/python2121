nome = (input("Digite seu nome; "))
def imc(peso, altura):
    imc =(round(peso / (altura**2)))
    return imc

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

resultado = imc (peso, altura)

print(nome)

if(resultado < 18.5):
    print("IMC = ", resultado, "Abaixo do peso")

elif(resultado >= 18.5) & (resultado < 25):
    print("IMC = ", round(resultado, 1), "Normal")

elif(resultado >= 25) & (resultado < 30):
    print("IMC = ", resultado, "Acima do peso")

else:
    print("IMC = ", resultado, "Obesidade")  