# 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого 
# треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок 
# окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли 
# треугольник разносторонним, равнобедренным или равносторонним.

# def triangle_type(a, b, c):
#     # Проверка существования треугольника
#     if a + b > c and a + c > b and b + c > a:
#         # Определение типа треугольника
#         if a == b == c:
#             return "Равносторонний"
#         elif a == b or a == c or b == c:
#             return "Равнобедренный"
#         else:
#             return "Разносторонний"
#     else:
#         return "Треугольника с такими сторонами не существует"

# a = float(input("Введите длину стороны a: "))
# b = float(input("Введите длину стороны b: "))
# c = float(input("Введите длину стороны c: "))

# result = triangle_type(a, b, c)
# print(result)

# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и 
# --чисел больше 100 тысяч.

# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# try:
#     number = int(input("Введите число (от 2 до 100000): "))
#     if number < 2 or number > 100000:
#         print("Число должно быть от 2 до 100000")
#     else:
#         if is_prime(number):
#             print(f"{number} - простое число")
#         else:
#             print(f"{number} - составное число")
# except ValueError:
#     print("Введите корректное целое число")

# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TARGET_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
MAX_ATTEMPTS = 10

print("Программа загадала число от 0 до 1000. Попробуйте угадать за 10 попыток.")

for attempt in range(MAX_ATTEMPTS):
    guess = int(input(f"Попытка {attempt + 1}/{MAX_ATTEMPTS}. Ваше предположение: "))
    
    if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
        print(f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}.")
        continue
    
    if guess < TARGET_NUMBER:
        print("Загаданное число больше вашего предположения.")
    elif guess > TARGET_NUMBER:
        print("Загаданное число меньше вашего предположения.")
    else:
        print(f"Поздравляем! Вы угадали число {TARGET_NUMBER} за {attempt + 1} попыток.")
        break
else:
    print(f"К сожалению, вы не угадали число {TARGET_NUMBER} за {MAX_ATTEMPTS} попыток. Правильный ответ был {TARGET_NUMBER}.")