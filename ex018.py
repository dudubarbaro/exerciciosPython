import math

angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}".format(angulo, seno))
print("O angulo de {} tem o COS de {:.2f}".format(angulo, cos))
print("O angulo de {} tem TANGENTE de {:.2f}".format(angulo, tangente))
