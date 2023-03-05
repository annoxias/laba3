
a=input("1 цвет")
b=input("2 цвет")
if a=="красный" and  b=="желтый" or a=="желтый" and b=="красный":
    print("оранжевый")
elif a=="красный" and  b=="синий" or a=="синий" and b=="красный":
    print("фиолетовый")
elif a=="желтый" and  b=="синий" or a=="синий" and b=="желтый":
    print("зеленый")
else:
    print("error")