"""Задание состоит из двух частей. 
вариант 30 1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.Вводятся К цифр. Составьте все возможные целые числа из этих цифр. Каждая цифра используется только 1 раз.
"""
"""
import itertools
import time
# Алгоритмический подход
def generate_integers_algorithmic(digits, S):
    # Преобразуем список цифр в строку
    digits_str = ''.join(digits)

    # Генерируем все возможные перестановки цифр
    permutations = list(itertools.permutations(digits_str))

    # Фильтруем перестановки по сумме цифр
    valid_permutations = [permutation for permutation in permutations if sum(int(digit) for digit in permutation) >= S]

    # Преобразуем каждую валидную перестановку в целое число
    integers = [int(''.join(permutation)) for permutation in valid_permutations]

    # Возвращаем список целых чисел
    return integers

# С использованием функций Python
def generate_integers_pythonic(digits, S):
    # Преобразуем список цифр в строку
    digits_str = ''.join(digits)

    # Генерируем все возможные перестановки цифр с помощью itertools.permutations
    permutations = itertools.permutations(digits_str)

    # Фильтруем перестановки по сумме цифр
    valid_permutations = [permutation for permutation in permutations if sum(int(digit) for digit in permutation) >= S]

    # Преобразуем каждую валидную перестановку в целое число
    integers = [int(''.join(permutation)) for permutation in valid_permutations]

    # Возвращаем список целых чисел
    return integers

# Получение ввода от пользователя
K = int(input("Введите количество цифр: "))
digits = [input("Введите цифру {}: ".format(i + 1)) for i in range(K)]
S = int(input("Введите минимальную сумму цифр: "))

# Замеряем время выполнения алгоритмического подхода
start_time_algorithmic = time.time()
integers_algorithmic = generate_integers_algorithmic(digits, S)
end_time_algorithmic = time.time()

# Замеряем время выполнения способа с использованием функций Python
start_time_pythonic = time.time()
integers_pythonic = generate_integers_pythonic(digits, S)
end_time_pythonic = time.time()

# Вывод результатов
print("Все возможные целые числа (алгоритмический подход):", integers_algorithmic)
print("Время выполнения алгоритмического подхода: {:.6f} секунд".format(end_time_algorithmic - start_time_algorithmic))

print("Все возможные целые числа (способ с использованием функций Python):", integers_pythonic)
print("Время выполнения способа с использованием функций Python: {:.6f} секунд".format(end_time_pythonic - start_time_pythonic))

# Находим максимальное целое число
max_integer = max(integers_algorithmic)

# Выводим результат
print("Максимальное целое число, которое можно составить из данных цифр с учетом ограничения на сумму цифр:", max_integer)
