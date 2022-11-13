# Функция 2
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# NumPy - это качественный и высокопроизводительный пакет для языка Python, предназначенный для научных вычислений в области
# многомерных массивов (в том числе и матриц), которые являются фундаментальной основой во многих научных направлениях.
# NumPy предоставляет большое количество высокоуровневых математических функций линейной алгебры, преобразования Фурье, случайных чисел и т.д.
# NumPy ориентирована на базовые вычисления и простую работу с матрицами
# NumPy не имеет дополнительных зависимостей, вместе с библиотекой не нужно ничего устанавливать.
import sympy as sym
# from sympy import symbols, sin, cos
# from sympy.plotting import plot
# SciPy — это библиотека для языка Python, основанная на расширении NumPy, но для более глубоких и сложных научных вычислений,
# анализа данных и построения графиков. SciPy в основном написана на Python и частично на языках C, C++ и Fortran,
# поэтому отличается высокой производительностью и скоростью работы.
# SciPy требует установки NumPy для корректной работы.
# в SciPy гораздо больше функций и методов, чем в NumPy
# SciPy предназначена для глубокого научного анализа
# Для ряда более простых задач она избыточна. Будет достаточно NumPy или других библиотек.
# Пакеты SciPy
# Возможности библиотеки распределены по нескольким модулям, или пакетам, которые объединены назначением.
# Это нужно, чтобы специалист мог подключить вместо полной библиотеки только требуемую часть. Так код будет эффективнее, а его написание — удобнее.
#
# Основные модули SciPy для научных вычислений:
#
# scipy.special — специальные функции, возможности и понятия из математической физики;
# scipy.integrate — функции для численного интегрирования и решения обыкновенных дифференциальных уравнений;
# scipy.optimize — алгоритмы оптимизации (в т.ч. минимизации математических функций);
# scipy.interpolate — методы для интерполяции, т.е. для приближенного нахождения какой-либо величины по уже известным отдельным ее значениям;
# scipy.fft — преобразования Фурье (операции, сопоставляющие одной функции вещественной переменной другую функцию вещественной переменной);
# scipy.signal — методы для обработки и преобразования сигналов;
# scipy.linalg — операции линейной алгебры. Модули с этим названием есть и в NumPy, и в SciPy, но их возможности различаются. В SciPy больше продвинутых функций и методов;
# scipy.sparse.csgraph — методы для работы с разреженными графами, особыми структурами данных;
# scipy.spatial — функции для работы с пространственными структурами данных и алгоритмами;
# scipy. stats — операции для статистических расчетов;
# scipy.ndimage — обработка многомерных изображений;
# scipy.io — ввод и вывод, загрузка и сохранение файлов.
# Пакеты необходимо импортировать отдельно.
# import scipy as sci
from scipy.optimize import fsolve as sci_fsolve
import matplotlib.pyplot as plt
import numpy

# описание глобальных переменных
funcrange = [-10, 10]
leftnum = min(funcrange)
rightnum = max(funcrange)


# Математическая функция в Python
# Это тригонометрическая функция, имеющая бесконечное количество корней.
# Можно определить корни только на заданном интервале.
def f(x):
    return -12 * x ** 4 * numpy.sin(
        numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


# нахождение корней на интервале
def solution():
    global leftnum, rightnum
    temp = leftnum
    rightnum = rightnum
    roots = []
    interval = []

    while temp < rightnum:
        # определяются интервалы, где функция переходит через 0
        if f(temp) >= 0 and f(temp + 1) <= 0:
            # scipy.optimize.fsolve - поиск корней функции. Первый агрумент - функция
            # Возвращает корни (нелинейных) уравнений, определяемых функцией func(x) = 0, учитывая начальную оценку аргумента
            # x0 - The starting estimate for the roots of func(x) = 0 (Начальная оценка корней func(x) = 0)
            w = sci_fsolve(f, temp)
            roots.append(*w)
        # определяются интервалы, где функция переходит через 0
        if f(temp) <= 0 and f(temp + 1) >= 0:
            w = sci_fsolve(f, temp)
            roots.append(*w)
        # если функция возрастает, добавляется список интервалов
        if f(temp) > f(temp + 1) < f(temp + 2):
            interval.append(temp + 1)
        temp += 1
    # список корней с округлением
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения для интервала от {leftnum} до {rightnum}: {roots}')

    return roots


# Определить промежутки, на которых f>0 и f<0:
def func_interval(left, right):
    array = []
    temp = left
    while left < right:
        array.append([f(left), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    else:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


# Вычисляем координаты вершины функции на заданном интервале:
def maxima_and_minima():
    # корни уравнения (точки, в которых значение функции равно нулю)
    roots = solution()
    if len(roots) < 2:
        print('На заданном интервале нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(func_interval(roots[i], roots[i + 1]))
        for j in top:
            j = [round(i, 2) for i in j]
            print(f'Координаты вершин функции: [{j[1]}, {j[0]}]')
        if len(top) < 2:
            print('error')
        else:
            for i in range(len(top) - 1):
                if top[i][0] > top[i + 1][0]:
                    print(f'На участке {round(top[i][0], 1)}...{round(top[i + 1][0], 1)} функция убывает')
                else:
                    print(f'На участке {round(top[i][0], 1)}...{round(top[i + 1][0], 1)} функция возрастает')


# График функции при помощи библиотеки matplotlib:
# начало интервала по x
start = -100
# конец интервала по x
finish = 100

x = [x for x in range(start, finish + 1)]
y = [(-12 * x ** 4 * sym.sin(sym.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
     x in range(start, finish + 1)]
# y = [y for y in range(-30, 30)]
plt.plot(x, y)
plt.grid()
# рисуем горизонтальную линию
plt.hlines(0, start, finish)
plt.title('graph using matplotlib')
plt.show()

# График функции при помощи библиотеки sympy:
# в диапазоне -300...300
# объявление символьной переменной x
x = sym.symbols('x')
# объявление функции y(x)
y = -12 * x ** 4 * sym.sin(sym.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
# Модуль построения графиков позволяет делать двухмерные и трехмерные графики.
# Графики отображаются с использованием matplotlib в качестве бэкэнда.
# аргумент show (boolean) - отображение графика. Можно управлять в процессе выполнения программы.
range_graph = (x, start, finish + 1)
sym.plot(y, range_graph, title='graph using sympy.plot', show=True)

# в диапазоне -10...10
# аргумент adaptive, по умолчанию установлено значение True.
# Для адаптивного значение установить False и указать аргумент nb_of_points, если требуется равномерная выборка.
# sym.plot(y, adaptive = False, nb_of_points = 1000)
sym.plot(y, adaptive=False, title='no adaptive')

# можно одновременно отображать графики нескольких функций
# extend(arg) - добавляет все описания из другого графика
y1 = 5 * x
y2 = 100 * x
y3 = x ** 2
p1 = sym.plot(y1, range_graph, show=False, title='Графики нескольких функций на одном plot (метод sym.plot)')
p2 = sym.plot(y2, range_graph, show=False)
p3 = sym.plot(y3, range_graph, show=False)
p2.extend(p3)
p1.extend(p2)
p1.show()

maxima_and_minima()
