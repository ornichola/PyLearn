﻿# [STEPIK]
# Программирование на Python https://stepik.org/67
# 01_12_02 Задачи по материалам недели

'''
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞)(−15,12]∪(14,17)∪[19,+∞) 
и False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы.

Sample Input 1:
20
Sample Output 1:
True

Sample Input 2:
-20
Sample Output 2:
False
'''

x = int(input())

if (x > - 15 and x <= 12) or (x > 14 and x < 17) or (x >= 19):
    print('True')
else:
    print('False')