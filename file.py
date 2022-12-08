#1

print("\nПравила:")
print("Ваша начальная позиция персонажа (0;0)")
print("Вам доступно указать направление персонажа: ВЛЕВО, ВПРАВО, НАЗАД или ВПЕРЕД,\nа так же указать количество шагов, чтобы переместить его.")

print("Какое направление вы выбрали?")
vector = input()

print("Сколько шагов вы хотите пройти?")
steps = int(input())

vectors_left = ['Влево', 'влево', 'налево', 'Налево', 'Лево', 'лево', 'ВЛЕВО']
vectors_right = ['Направо', 'направо', 'право', 'Право', 'ВПРАВО','Вправо', 'вправо']
vectors_up = ['Наверх', 'наверх', 'вверх', 'Вверх', 'ВПЕРЕД', 'Вперед', 'НАВЕРХ', 'ВВЕРХ']
vectors_down = ['Вниз', 'вниз', 'низ', 'Низ', 'Назад', 'назад', 'НАЗАД', 'ВНИЗ', 'НИЗ']

if steps < 0:
    print("Количество шагов не может быть отрицательным!")
else:
    if vector in vectors_left:
        print(f"Ваша позиция персонажа теперь ({0 - steps};0)")
    elif vector in vectors_right:
        print(f"Ваша позиция персонажа теперь ({0 + steps};0)")
    elif vector in vectors_up:
        print(f"Ваша позиция персонажа теперь (0;{0 + steps})")
    elif vector in vectors_down:
        print(f"Ваша позиция персонажа теперь (0;{0 - steps})")
    else:
        print("Возможно, вы ошиблись в написании направления, посмотрите возможные варианты в правилах!")

#2

vectors_left = ['Влево', 'влево', 'налево', 'Налево', 'Лево', 'лево', 'ВЛЕВО']
vectors_right = ['Направо', 'направо', 'право', 'Право', 'ВПРАВО','Вправо', 'вправо']
vectors_up = ['Наверх', 'наверх', 'вверх', 'Вверх', 'ВПЕРЕД', 'Вперед', 'НАВЕРХ', 'ВВЕРХ']
vectors_down = ['Вниз', 'вниз', 'низ', 'Низ', 'Назад', 'назад', 'НАЗАД', 'ВНИЗ', 'НИЗ']

print("\nПравила:")
print("Ваша начальная позиция персонажа (0;0)")
print("Вам доступно указать направление персонажа: ВЛЕВО, ВПРАВО, НАЗАД или ВПЕРЕД,\nа так же указать количество шагов, чтобы переместить его.")
print('Чтобы остановить игру введите после вопроса "Какое направление вы выбрали?" слово \"stop\".')

x = 0
y = 0

while True == True:
    print("Какое направление вы выбрали?")
    vector = input()
    if vector == "stop":
        break
    print("Сколько шагов вы хотите пройти?")
    steps = int(input())
    if steps < 0:
        print("Количество шагов не может быть отрицательным!")
    else:
        if vector in vectors_left:
            x -= steps
            print(f"Ваша позиция персонажа теперь ({x};{y})")
        elif vector in vectors_right:
            x += steps
            print(f"Ваша позиция персонажа теперь ({x};{y})")
        elif vector in vectors_up:
            y += steps
            print(f"Ваша позиция персонажа теперь ({x};{y})")
        elif vector in vectors_down:
            y -= steps
            print(f"Ваша позиция персонажа теперь ({x};{y})")
        else:
            print("Возможно, вы ошиблись в написании направления, посмотрите возможные варианты в правилах!")

#3

import cmath as m
print("Решение квадратного уравнения вида a*x^2 + b*x + c = 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
x = 0
D = b**2 - 4*a*c
if D < 0:
    print("Вещественных корней нет")
if D == 0:
    х = (-b / 2*a)
    print(f"x = {x}")
if D > 0:
    x1 = (-b + int(m.sqrt(D).real))/(2*a)
    x2 = (-b - int(m.sqrt(D).real))/(2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

#4

import cmath as m
print("Решение квадратного уравнения вида a*x^2 + b*x + c = 0")
a = input("a = ")
b = input("b = ")
c = input("c = ")
if a[-1] == "j" or b[-1] == "j" or c[-1] == "j":
    a = complex(a)
    b = complex(b)
    c = complex(c)
    x = 0
    D = b**2 - 4*a*c
    x1 = (-b + m.sqrt(D))/(2*a)
    x2 = (-b - m.sqrt(D))/(2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
else:
    a = int(a)
    b = int(b)
    c = int(c)
    x = 0
    D = b**2 - 4*a*c
    if D < 0:
        x1 = (-b + m.sqrt(D))/(2*a)
        x2 = (-b - m.sqrt(D))/(2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    if D == 0:
        х = (-b / 2*a)
        print(f"x = {x}")
    if D > 0:
        x1 = (-b + int(m.sqrt(D).real))/(2*a)
        x2 = (-b - int(m.sqrt(D).real))/(2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")