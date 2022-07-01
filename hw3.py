from mod1 import levenshtein_func as lf, compare, morf_compare as mc

s1 = input('Введите строку 1: ')
s2 = input('Введите строку 2: ')

a = mc(s1,s2)
if a > 0.9:
    print('Строки не отличаются. Показатель сравнения равен: ',a)
else: 
    print('Строки отличаются на - ',lf(s1,s2), ' символов')
