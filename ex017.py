import math

cOposto = float(input("Comprimento do cateto oposto: "))
cAdjacente = float(input("Comprimento do cateto Adjacente: "))

hipotenusa = math.hypot(cOposto, cAdjacente)

print("A hipotenusa vai medir {:2f}".format(hipotenusa))
