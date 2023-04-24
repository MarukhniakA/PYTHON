login = str(input("Введите логин: "))

def decorator(func):
    def wrapper(*args, **kwargs):
        if login == "admin":
            func(*args, **kwargs)
        if login != "admin":
            return print("Доступ запрещен!")
    return wrapper

@decorator
def my_func(check):
    print("Сумма на вашем счете: {} рублей".format(check))
my_func(100)