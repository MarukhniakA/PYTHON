
a = 0 or int(input("Введите первое число: ")) 
b = 0 or int(input("Введите второе число: ")) 
c = 0 or int(input("Введите третье число: ")) 

nnz = a and b and c and "Нет нулевых значений!!!"
print(nnz)
vvn = a or b or c or "Введены все нули!"
print(vvn)

if a > (b + c):
    print(a - b - c)
print("Задание 3")  
  
if a < (b + c):
    print(b + c - a)
print("Задание 4")     

 
if a > 50 and ((b or c) > a):
    print("Вася")
print("Задание 5")    

if a > 5 or ((b and c ) == 7):
    print("Петя")
print("Задание 6")      
