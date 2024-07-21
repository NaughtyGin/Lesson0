print(5)
print(type(5))
print(5//5)
print(5/5)
print(int(5/5)) # int - тип данных "целочисленные" (integra)
print(   +5+   +3)
print(5//4), print(5/4) # "//" - целочисленное деление, "/" - деление (получаются числа "с плавающей запятой"
# !!! как сделать, чтобы печатало на одной строке?
print(5%4) # % - остаток от деления
print(       2.0) # float - тип данных "с плавающей запятой"
# "пробел" не имеет значения для чисел - не печататется в результате
print(type(2.0))
print('Hello, world')
print(type(('Hello, world')))
print('1'+ '     1') #concatenate - конкатенация ("сложение" или "склеивание" для типа данных str - "строка", по сути - "текст"
# "пробел" имеет значение для данных типа str (печатается в результате)
print(True, '      ', False) # "пробел" печатается, если взять его в кавычки (тип данных str)
print(True+False) # логические (булевы) данные, тип bool (boolean)
# Ложь + Истина = 1
print(type(True),type('False')) # цветом выделяются разные типы данных: голубой - числа, зеленый - текст, оранжевый - логический тип
print(5>10,10>5)
print(5==5, '       ', 5!=5) # "==" - логическое равенство объектов, "!=" - неравенство объектов
print(5>10 or 10>5) # логическое И ("and") и логическое ИЛИ ("or"): для И должны быть истинными ВСЕ выражения, для ИЛИ достаточного одного - чтобы результат был ИСТИНА (True)
print(5>10 and 5<10 or 5!=5)
print(5>10 or 5<10 or 5!=5)
print(5>10 or 5<10 and 5!=5)
print(5>10 or 5<10 and 5==5)
print(5<10 and 5!=5)
print(5<10 or 5!=5)
print(5>10 or 5!=5)
print(5<10 and 5==5)
print(int('5')) # для преобразования типа данных используется тот тип данных, который нужен
print(type(int('5')))
print(5>3, type(str(5>3)))