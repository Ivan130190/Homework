'''
Угадай число
'''
import random
number = random.randint(1,50)

user =-1
while user!=number:
    user=int(input("Угадай число от 1 до 50"))
    if user > number:
        print("Число должно быть меньше!")
    elif user < number:
        print("Число должно быть больше!")
    else:
        print("Вы угадали число = " +str(number))
        break

'''
Калькулятор
'''

print('Введите число a=')
a = int(input())
print('Введите число b=')
b = int(input())
print('Выбирите операцию')
print('1 - сложение a+b')
print('2 - вычитание a-b')
print('3 - деление a/b')
print('4 - умножение a*b')
d = float(input())
if d == 1:
    print('Сумма a+b=',a+b)
if d == 2:
    print('Разность a-b=',a-b)
if d == 3:
    print ('Частное a/b=',a/b)
if d == 4:
    print('Произведение a*b=',a*b)

'''
Черепашка (Прямоугольник)
'''
import turtle
a = turtle.Turtle()
a.forward(100)
a.left(90)
a.forward(50)
a.left(90)
a.forward(100)
a.left(90)
a.forward(50)
print(a)
'''
Черепашка (Квадрат)
'''
import turtle
a = turtle.Turtle()
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)
a.forward(50)
print(a)
