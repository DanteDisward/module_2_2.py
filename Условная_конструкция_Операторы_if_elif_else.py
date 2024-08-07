import re #Импортируем библиотеку

while True: #Запускем бесконечный цикл
    try:
        first, second, third = re.split(r'[,; ]+', input("Введите три числа: ")) #Просим ввести данные и разделяем строку на несколько значений
        first = int(first)
        second = int(second)
        third = int(third)
        break #Если всё впорядке, останавливаем цикл
    except ValueError:
        print("Вы допустили ошибку") #Если данные не правильно ввели, выводим соответствующее сообщение
#Проверяем сколько чисел равны между собой
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)

