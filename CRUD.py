dictionary = {"1": {
         'id':'1',
         'имя':'Влад',             
         'пол':'муж',
         'возраст':'23',
         'рост':'180',
         'вес':'82'
         },
          "2": 
         {'id':'2',
         'имя':'Настя',
         'пол':'жен',
         'возраст':'22',
         'рост':'172',
         'вес':'52'},
         "3": 
          {'id':'3',
         'имя':'Карина',
         'пол':'жен',
         'возраст':'21',
         'рост':'175',
         'вес':'72',
         },
          "4": 
          {'id':'4',
         'имя':'Денис',         
         'пол':'муж',
         'возраст':'22',
         'рост':'181',
         'вес':'83',
         }
         }

def clear():
  import os
  os.system("CLS")
  
def menu():
    print("Menu:")
    print(" A. Вывести список пользователей.")
    print(" B. Посмотреть информацию о пользователях.")
    print(" C. Изменить данные о пользователе.")
    print(" D. Удалить выбранного пользователя.")
    print(" E. Добавить пользователя.")
    print(" F. Выход")
    vibor = str(input("Выберите пункт: "))
    clear()
    return vibor

def spisok():
    print(dictionary.keys())

def info():
    info_user_key = input("Введите id пользователя: ") 
    print(dictionary.get(info_user_key), "Нет такого пользователя!")
    
def change():
    dictionary[input('Введите id, которое хотите изменить: ')][input('Введите, какие данные хотите изменить: ')] = input('Введите, на что хотите поменять: ')
    print(dictionary)

def delete():
    delete_user = input("Введите id пользователя, которого хотите удалить: ")
    print(dictionary.pop(delete_user))

def add():
    key = input("Введите id")
    name = input("Введите ваше имя: ")         
    floor = input("Введите ваш пол: ")
    age = input("Введите ваш возраст: ")
    height = float(input("Введите ваш рост в см: "))
    weight = float(input("Введите ваш вес: "))
    dictionary[key] = [name, floor, age,  height, weight] 
    print(dictionary)


def option_menu():
        ortion_menu_user = menu() 
        if ortion_menu_user == str("A"):
            spisok()
        elif ortion_menu_user == str("B"):
            info()
        elif ortion_menu_user == str("C"):
            change()
        elif ortion_menu_user == str("D"):
            delete()
        elif ortion_menu_user == str("E"):
            add()
        elif ortion_menu_user == str("F"):
            exit()
        
def itog():
    while option_menu != "stop":
        option_menu()    
        
itog()            