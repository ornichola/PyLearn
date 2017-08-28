#[STEPIK]
# Программирование на Python https://stepik.org/67
# 3.5.3 Модули, подключение модулей

'''
Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.

Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.

Пример работы программы:

> python3 my_solution.py arg1 arg2
arg1 arg2
'''

import sys

for i in range(1, len(sys.argv)):
	print(sys.argv[i], end = ' ')

'''
import sys
print(*sys.argv[1:])
'''