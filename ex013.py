salario = float(input("Qual é o salário do Funcionário? R$"))
aumento = salario + (salario * 0.15)

print(
    "Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}".format(
        salario, aumento
    )
)
