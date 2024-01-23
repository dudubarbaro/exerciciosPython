km = float(input("Quantos km foram rodados? "))
diaria = float(input("Quantos dia de aluguel? "))

precoDiaCarro = diaria * 60
precoKmRodado = km * 0.15

precoTotal = precoDiaCarro + precoKmRodado

print("O valor total do alguel é de {}".format(precoTotal))
