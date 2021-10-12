# 3_1  Стандартные методы и функции для строк
'''
Реализация задачи на нахождение количества вхождений подстроки в строку, с пересечением подстроки
т.е. пример строка 'abababa' и подстрока 'aba', есть пересечение и в этом случае, counter = 3,
при вызове метода s.count(t) результат = 2
'''

# s - строка
# t - подстрока
# counter - счетчик
# ind - индекс(индекс начала вхождения подстроки)


s, t, counter, ind = input(), input(), 0, 1
while ind != -1:
    ind = s.find(t)
    if ind >= 0:
        counter += 1
    s = s[ind+1:]
print(counter)
