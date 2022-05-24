'''
1) Прочитано
2)Написать список мужских и женских имён,вывести только женские имена
'''
Name_m_w = ['Koly','Kristina','Vika','Vany','Igor','Alina','Makar','Oly','Maksim','Natasha']
print(Name_m_w[1:3], Name_m_w[5], Name_m_w[7], Name_m_w[-1])
'''
3) Написать генератор списка, который создаст список, состоящий только из элементов с нечётным кол-ом цифр
'''
import random
a = [random.randint(1,250) for i in range(1,10)]
print (a)
b = [i for i in a if len(str(i))%2 ==1 ]
print(b)



