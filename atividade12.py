n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))
me = float(input("Qual a média da sua instituição?: "))

ma = (n1 + n2 * 2 + n3 * 3 + me)/7
ma = round(ma, 0)

if ma >= 90:
  print("(A)", ma, "Aprovado")

elif ma >= 75 and ma < 90:
  print("(B)", ma, "Aprovado")

elif ma >= 60 and ma < 75:
  print("(C)", ma, "Aprovado")

elif ma >= 40 and ma < 60:
  print("(D)", ma, "Reprovado")
  
else:
  print("(E)", ma, "Reprovado")