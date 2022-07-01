from Levenshtein import distance
from pymorphy2 import MorphAnalyzer
import pprint

def levenshtein_func(s1,s2):
    r = distance(s1, s2)
    return r

def compare(s1,s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count / max(len(s1), len(s2))

def morf_compare(s1,s2):
    ma = MorphAnalyzer()
    
    m_s1 = ma.parse(s1)[0].normal_form
    m_s2 = ma.parse(s2)[0].normal_form
    print(m_s1, ' ', m_s2)

    return compare(m_s1, m_s2)

if __name__ == '__main__':
    pairs = [
        ('kitten','sitting'),
        ('saturday','sunday'),
        ('море','гора'),
        ('компьютер','компьютеризация'),
        ('компьютер','компьютеры'),
    ]

    for s, t in pairs:
        print(s, t, levenshtein_func(s,t), compare(s,t), morf_compare(s,t))

