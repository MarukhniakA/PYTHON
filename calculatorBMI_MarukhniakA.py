height = float(input("Введите свой рост в см: "))
weight = float(input("Введите свой вес в кг: "))
h = height / 100
bmi = int(weight/(h * h))
print("Ваш индекс массы тела: " + str(bmi))
scale = ["16", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "40"]
d = scale[1:-1]
i = int((bmi - 16)/((40 - 16)/len(d)))
scale.insert(i,"|")
print(" ".join(scale))