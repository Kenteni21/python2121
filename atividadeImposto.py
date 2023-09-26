bruto = float(input("Insira seu salario bruto: "))

if bruto <= 2112:
  print("Não paga imposto")

elif bruto <= 2826.65:
  descontado = bruto * 0.075
  bruto_descontado = bruto - descontado
  print("Seu salario liquido é:", bruto_descontado, "Alíquota de 7,5%")

elif bruto <= 3751.05:
  descontado = bruto * 0.15
  bruto_descontado = bruto - descontado
  print("Seu salario liquido é:", bruto_descontado, "Alíquota de 15%")

elif bruto <= 4664.68:
  descontado = bruto * 0.225
  bruto_descontado = bruto - descontado
  print("Seu salario liquido é:", bruto_descontado, "Alíquota de 22.5%")

else:
  descontado = bruto * 0.275
  bruto_descontado = bruto - descontado
  print("Seu salario liquido é:", bruto_descontado, "Alíquota de 27.5%")
