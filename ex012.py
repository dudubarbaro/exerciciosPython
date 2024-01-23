preco = float(input("Qual é o preço do produto? R$"))
promo = preco - (preco * 0.05)

print(
    "O produto que custava R${}, na promoção com desconto de 5% vai custar R${}".format(
        preco, promo
    )
)
