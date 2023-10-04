#1
#a='Задача «Делаем срезы»'
#print(a[2])
#print(a[-1])
#print(a[:5])
#print(a[:-2])
#print(a[1::2])
#print(a[::2])
#print(a[::-1])
#print(a[-1:0:-2])
#print(len(a))

#2 Задача «Количество слов»
#print('количество слов','Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count'.count(' ') +1)

#3 Две половинки
# line=input('Две половинки:  ')
# half=len(line) //2 +len(line)%2
# halfed= line[half:-1] + ' ' +line[:half]
# print(halfed)

#4 Первое и последнее вхождения
# f_Ki = input(' Первое и последнее вхождения:   ')
# print('если -1 то это означает что тут нет \'f\'')
# print(f_Ki.find('f'))
# print(f_Ki.rfind('f'))

#5 Удаление фрагмента
# h=input('Удаление фрагмента h ( не меньше дыух h):   ')
# h1=h.find('h')
# h2=h.rfind('h')
# h_dalete=h[h1:h2+1]
# print(h.replace(h_dalete, ''))

#6 Замена подстроки
# one=input('Замена подстроки:   ')
# print(one.replace('1', 'one'))

# 7 Удаление символа
# dalete=input('Удаление символа @:   ')
# print(dalete.replace('@', ''))

#8 Замена внутри фрагмента
# dalete=input('Замена внутри фрагмента:   ')
# h1=dalete.find('h')
# h2=dalete.rfind('h')
# concatination=dalete[h1+2:h2]
# fixed=concatination.replace('h', 'H')
# con1=dalete[:h1+1]
# con2=dalete[h2:]
# print(con1 + fixed + con2)

###############################
#Синтаксис условной инструкции#
###############################

#1 Минимум из двух чисел
# first=1321
# second=3212
# if first>second:
#     print(first)
# else: print(second)

#2 Знак числа
# signX=int(input('чему равна будет:  '))
# if signX>0:
#     print('sign_x = 1')
# elif signX < 0:
#     print('sign_x = -1')
# else:
#     print('sign_x = 0')

#3 Шахматная доска
# x1 = int(input("Введите номер столбца первой клетки (от 1 до 8): "))
# y1 = int(input("Введите номер строки первой клетки (от 1 до 8): "))
# x2 = int(input("Введите номер столбца второй клетки (от 1 до 8): "))
# y2 = int(input("Введите номер строки второй клетки (от 1 до 8): "))
#
# if (x1 + y1) % 2 == (x2 + y2) % 2:
#     print("YES")
# else:
#     print("NO")

#4 високосный год
# date=int(input('введите число для нахождения високосности:  '))
# if date % 400 == 0:
#     print('EYS')
# elif date%100==0:
#     print('NO')
# elif date%4==0:
#     print('EYS')
# else:
#     print('NO')

#5 Сколько совпадает чисел
# #number1=int(input('введите 1 число:  '))
# number2=int(input('введите 2 число:  '))
# number3=int(input('введите 3 число:  '))
# if number1==number2 and number1==number3:
#    print(number1, number3, number2, str('совпали все числа'))
# elif number1==number2:
#    print('совпали первое и второе число: ', number1, number2)
# elif number2==number3:
#    print('совпали второе и тртье число: ', number2, number3)
# elif number1==number3:
#    print('совпали первое и третье: ', number1, number3)
# else:
#    print('ни одно число не совпало')

#6 Ход ладьи
# x1 = int(input("Введите номер столбца первой клетки (от 1 до 8):  "))
# y1 = int(input("Введите номер строки первой клетки (от 1 до 8):  "))
# x2 = int(input("Введите номер столбца второй клетки (от 1 до 8):  "))
# y2 = int(input("Введите номер строки второй клетки (от 1 до 8):  "))
# if x1==x2 or y1==y2:
#     print('YES')
# else:
#     print('NO')

#7 Шоколадка
# n=int(input('кол-во долек по вертикали:  '))
# m=int(input('кол-во долек по горизонтали;  '))
# k=int(input('кол-во долек:  '))
# if n%k==0 or m%k==0:
#     print('YES')
# else:
#     print('NO')

#8 Яша плавает в бассейне
# M=int(input('длина бассейна:  '))
# N=int(input('ширина бассейна:  '))
# x=int(input('где Яша находится по длине?:  '))
# y=int(input('где Яша находится по ширине?:  '))
#
# if x<M-x:
#     x=x
# else:
#     x=M-x
# if y<N-y:
#     y=y
# else:
#     y=N-y
# if x<y:
#     print('x наименьшее расстояние до бортиков: ',x)
# else:
#     print('y наименьшее расстояние до бортиков: ',y)
