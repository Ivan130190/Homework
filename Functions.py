# Создать пустую функцию которая не чего не возвращает.
def fun (a,b):
    return a,b
print(fun(2,3))

# Написать функцию, которая принимает число, возвращает его значение умноженное на два.
def fun (a):
    return a*2
print(fun(10))
# Написать функцию, которая определяет параметры на чётность.
def number(x):
    return x % 2 ==0
print(number(5))
# Функция принимает два аргумента. После чего проверим, если первое число >10, принтим (Да). Если < (Нет)
def func(a,b):
    if a>=10:
        print("Да")
    if a<=10:
        print("Нет")
print (func(60,30))
# Написать лямбда функцию, которая делит два аргумента
g = lambda v,j: v/j
print(g(2,3))
# Использовать ф-ю map и filter
#map
numbers = [2,6,9,1,2,6,7,5,2,9]
def klon(l):
    return l / 2
numbers = list(map(klon,numbers))
print(numbers)
#filter
numbers_2 = [2,65,26,48,548,3,4,9,91,36,46]
def zer (p):
    return p<=40
numbers_2 = list(filter(zer,numbers_2))
print(numbers_2)
# Поиск мах и min  в списке
List1 = ["Анастасия","Вечеслав","Иван", "Геннадий","Кристина"]
max_str = max(List1, key=len)
min_str = min(List1, key=len)
print("Самое длинное имя",max_str)
print("Самое короткое имя", min_str)
# Всокосный ли год
year = int(input ( "Введите год" ))
if year % 4 !=0:
    print(" Год не високосный.")
elif year % 100 ==0:
    if year % 400 ==0:
        print("Год високосный.")
    else:
        print("Год не високосный.")
else:
    print("Год високосный.")
# Функция season
def season(num):
   if num == 12 or 1 <= num <= 2:
       print("Зима")
   elif  3 <= num <= 5:
       print("Весна")
   elif 6 <= num <= 8:
       print("Лето")
   elif 9 <= num <= 11:
       print("Осень")
   else:
       print("Неверно введён номер месяца!")
n = int(input("Введите номер месяца (1-12): "))
season(n)

# Функция date
from datetime import date
def foo(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False
print(foo(1768, 2, 28))
print(foo(1768, 2, 29))



