from Levenshtein import distance
from pymorphy2 import MorphAnalyzer
from mod1 import compare

class St():

    def __init__(self, st1, st2):
        print('Создание объекта')
        ma = MorphAnalyzer()
    
        self.st1 = st1
        self.st2 = st2    
        self.m_st1 = ma.parse(st1)[0].normal_form
        self.m_st2 = ma.parse(st2)[0].normal_form


    def degree_like(self):

        # сравниваем строки в нормальной форме для определения уровня схожести
        c = compare(self.st1, self.st2)

        # находим отличия в строках изначального вида
        otl = distance(self.st1, self.st2)

        # вывод степени схожести и кол-во символов отличия
        print('Уровень схожести =  ', c, ', Строки отличаются на ',otl,' символов')

if __name__ == '__main__':
    pairs = [
        ('kitten','sitting'),
        ('saturday','sunday'),
        ('море','гора'),
        ('компьютер','компьютеризация'),
        ('компьютер','компьютеры'),
        ]

    for s, t in pairs:
        st = St(s, t)
        st.degree_like()
                

