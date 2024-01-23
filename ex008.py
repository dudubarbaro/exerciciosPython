distancia = int(input("Uma distancia em metros: "))

km = distancia / 1000
hm = distancia / 100
dcm = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print("A medida de {}m corresponde a".format(distancia))
print("{}km".format(km))
print("{}hm".format(hm))
print("{}dcm".format(dcm))
print("{}dm".format(dm))
print("{}cm".format(cm))
print("{}mm".format(mm))
