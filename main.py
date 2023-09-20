import math
menu = 0
while menu != 11:
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")
    print("5.Возведение в степень")
    print("6.Квадратный корень")
    print("7.Факториал")
    print("8.Синус")
    print("9.Косинус")
    print("10.Тангенс")
    print("11.Выход из программы")
    try:
        menu = int(input())
    except ValueError:
        print("Введите число от 1 до 11")
    match menu:
        case 1:
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                print("Ответ:", ' ', a + b)
            except ValueError:
                print("Вводите только числа")
        case 2:
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                print("Ответ:", ' ', a - b)
            except ValueError:
                print("Вводите только числа")
        case 3:
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                print("Ответ:", ' ', a * b)
            except ValueError:
                print("Вводите только числа")
        case 4:
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                if b == 0:
                    print("На ноль делить нельзя")
                else:
                    print("Ответ:", ' ', a / b)
            except ValueError:
                print("Вводите только числа")
        case 5:
            try:
                print("Введите число:")
                a = float(input())
                print("Введите степень:")
                n = int(input())
                print("Ответ:", ' ', a ** n)
            except ValueError:
                print("Неверно введено число")
        case 6:
            try:
                print("Введите число:")
                a = float(input())
                if a < 0:
                    print("Введено число меньше нуля")
                else:
                    print("Ответ:", ' ', math.sqrt(a))
            except ValueError:
                print("Вводите только числа")
        case 7:
            try:
                print("Введите целое число:")
                a = int(input())
                if a < 0:
                    print("Введено число меньше нуля, возможно введено нецелое число")
                else:
                    print("Ответ:", ' ', math.factorial(a))
            except ValueError:
                print("Неверно введене число")
        case 8:
            try:
                print("Введите число:")
                a = float(input())
                if a > 1 or a < -1:
                    print("Число должно быть от -1 до 1")
                else:
                    print("Ответ:", ' ', math.sin(a))
            except ValueError:
                print("Вводите числа от -1 до 1")
        case 9:
            try:
                print("Введите число:")
                a = float(input())
                if a > 1 or a < -1:
                    print("Неверно введено число")
                else:
                    print("Ответ:", ' ', math.cos(a))
            except ValueError:
                print("Вводите числа от -1 до 1")
        case 10:
            try:
                print("Введите число:")
                a = int(input())
                print("Ответ:", ' ', math.tan(a))
            except ValueError:
                print("Вводите только числа")
