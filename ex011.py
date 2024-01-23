lg = float(input("Largura da Parede: "))
alt = float(input("Altura da Parede: "))

area = lg * alt
tinta = area / 2

print("Sua parede tem a dimensão de {}X{} e sua área é de {}m²".format(lg, alt, area))
print("Para pintar essa parede, você precisará de {}l de tinta".format(tinta))
