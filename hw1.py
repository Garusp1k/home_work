# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

# author_name = 'Александр'
# author_location = 'на Сахалине'
# author_location_square = '76 400 км²'
# author_location_population = 488257
#
# print(f'Добрый день, меня зовут {author_name} и я живу {author_location}.\n'
#       f'Сахалин крупнейший остров России. Его площадь составляет {author_location_square}')
# user_name = input('А как зовут Вас?\n>>>')
#
# print(f'Приятно познакомиться {user_name}')
#
# user_location = input('Где вы проживаете?\n>>>')
# user_location_population = input('Численность населения в Вашем регионе?\n>>>')
#
# if user_location_population.isdigit():
#     user_location_population = int(user_location_population)
# else:
#     print(user_name, 'укажите, пожалуйста, количество людей в числовом формате')
#     exit()
#
# if author_location_population > user_location_population:
#     print(f'{author_location} живет больше людей')
# elif author_location_population == user_location_population:
#     print('Удивительное совпадение!')
# else:
#     print(f'В {user_location} людей больше чем {author_location}')


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

# time = input('Введите время в секундах: ')
# duration_hour = 3600
# duration_minutes = 60
#
# if time.isdigit():
#     time = int(time)
# else:
#     print('Укажите, пожалуйста, время в числовом формате')
#     exit()
#
# hour = time // duration_hour
#
# if time >= duration_hour:
#     minutes = int(abs(time - duration_hour) / duration_minutes)
# else:
#     minutes = time//duration_minutes
#
# # minutes = int(abs(time - duration_hour) / duration_minutes)  # не понятен перевод в минуты
# second = (time - duration_hour) % duration_minutes
#
# print(f'При вводе {time} секунд получается:\n{hour}: {minutes}: {second}')


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Простейший способ
# number_version_1 = int(input('Введите число N: '))
# summ_version_1 = (number_version_1 + (number_version_1 * 11) + (number_version_1 * 111))
# print('Версия первая: ', summ_version_1)
#
# # Так как при делении суммы чисел на N при любом раскладе получается 123
# number_version_2 = int(input('Введите число N: '))
# summ_version_2 = (number_version_2 * 123)
# print('Версия вторая: ', summ_version_2)
#
# # Корректный способ
# one_number = int(input('Введите число N: '))
# step = str(one_number)
# double_number = step + step
# triple_number = step + step + step
# summ_version_3 = one_number + int(double_number) + int(triple_number)
# print('Версия третья: ', summ_version_3)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

number = int(input('Введите целое положительное число: '))
max = number % 10
while number>=1:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number > 9:
        continue
    else:
        print('Максимальная цифра в числе: ', max)
        break


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
