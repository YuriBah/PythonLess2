my_price = [57.8, 46.51, 97, 100, 27.50, 48.90, 50.03, 66.20, 99, 123.50]
for i in my_price:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):2d} коп,")