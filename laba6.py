"""Задание состоит из двух частей. 
вариант 30 1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.Вводятся К цифр. Составьте все возможные целые числа из этих цифр. Каждая цифра используется только 1 раз.
"""
import itertools
import timeit

# Алгоритмический подход
def generate_numbers_alg(digits):
    numbers = []
    _generate_numbers_alg(digits, '', numbers)
    return numbers

def _generate_numbers_alg(digits, current_number, numbers):
    if not digits:
        numbers.append(int(current_number))
    else:
        for i, digit in enumerate(digits):
            _generate_numbers_alg(digits[:i] + digits[i+1:], current_number + digit, numbers)

# Функциональный подход с использованием itertools
def generate_numbers_itertools(digits):
    return [int(''.join(number)) for number in itertools.permutations(digits)]

# Генерация случайного набора цифр
K = int(input("Введите количество цифр K: "))
digits = [str(i) for i in range(1, K + 1)]

# Сравнение времени выполнения двух подходов
start_time_alg = timeit.default_timer()
numbers_alg = generate_numbers_alg(digits)
time_alg = timeit.default_timer() - start_time_alg

start_time_itertools = timeit.default_timer()
numbers_itertools = generate_numbers_itertools(digits)
time_itertools = timeit.default_timer() - start_time_itertools

print("Алгоритмический подход:")
print(numbers_alg)
print("Время выполнения: {:.6f} секунд".format(time_alg))

print("\nПодход с использованием itertools:")
print(numbers_itertools)
print("Время выполнения: {:.6f} секунд".format(time_itertools))

