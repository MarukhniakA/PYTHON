pred = "Не знаю, как там в Лондоне, я не была. Может, там собака - друг человека. А у нас управдом - друг человека!"
print(pred)
print ("1. Количество символов: " + str (len(pred))) 
print("2.Развернутая строка: " + str(pred [::-1]))
print ("3.Каждое слово с большой буквы: " + str(pred.title()))
print ("4.Текст прописными буквами: " + str(pred.upper()))
print("5.Число вхождений 'нд', 'ам', 'о' в строку : " + str(pred.count("нд")) + str(pred.count("ам")) + str(pred.count("о")))
print("6.Дублирование строки:" + str(pred)*3)
print("6.Извлечение среза:" + str(pred[8:15]))
per = ''.join(reversed(pred))
print("7.Развернутое предложение:" + str(per))
print ("8.Исходная строка: " + pred)



print("6.Дублирование строки:" + str(pred)*3)
print("6.Извлечение среза:" + str(pred[8:15]))
per = ''.join(reversed(pred))
print("7.Развернутое предложение:" + str(per))
print ("8.Исходная строка: " + pred)
