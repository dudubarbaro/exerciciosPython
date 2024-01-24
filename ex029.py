velo = int(input("Qual é a velocidade atual do carro? "))
if velo > 80:
    print("multado!")
    multa = (velo - 80) * 7
    print("O valor da multa é {:.2f}".format(multa))
print("OK! SIGA!")