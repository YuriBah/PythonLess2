my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_processing = []

for i in my_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            list_processing.append(f"'{int(i):02}'")
        else:
            list_processing.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        list_processing.append(i)

print(list_processing)
print("".join(list_processing))