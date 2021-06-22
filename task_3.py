'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the
'''


result = []
d = int(input())
s = [input().lower() for i in range(d)]

l = int(input())
s1 = [input().lower().split(' ') for j in range(l)]

[result.append(i) for row in s1 for i in row if i not in s]


[print(i) for i in set(result)]