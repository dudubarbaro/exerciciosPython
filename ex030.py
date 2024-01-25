l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Ok, pode se formar um triãngulo!")
    if l1 == l2 == l3:
        print("Equilátero")
    elif l1 != l2 != l3 != l1:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os segmentos não podem formar um triângulo!")
