my_price = [57.8, 46.51, 97, 100, 27.50, 48.90, 50.03, 66.20, 99, 123.50]

#--------------------------A---------------------------
for i in my_price:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):2d} коп,")

#--------------------------B---------------------------

print(f"\n\n{'*'* 35} B\n")
print(f"ID base: {id(my_price)} - {my_price}")
my_price.sort()
print(f"ID change: {id(my_price)} - {my_price}")

#-------------------------C & D------------------------

print(f"\n{'*' * 35} C & D\n")
print(f"ID change: {id(sorted(my_price))} - {sorted(my_price, reverse=True)}\n{sorted(my_price)[-5:]}")

