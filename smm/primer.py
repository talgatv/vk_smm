
# coding: utf-8

# In[2]:


import requests
import csv
import time
import sqlite3


group_id = 38369814
offset = 0
count = 1001 #потом переопределим


a = [] # первая отсечка
b = [] # вторая отсечка

#сбор списка пользователей на начало периода

print('цикл А')
while offset < count:
    r = requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id': group_id,
                                                                           'offset':offset}).json()

    response = r['response']
    count = response['count']

    a.extend(response['users'])

    offset = offset + 1000
    print(offset)
    time.sleep(0.37)
print('first done')

#засыпаем на 10 минут
print('Time sleep 10 minuts')
time.sleep(10)

#сбор списка пользователей на конец периода

offset = 0
count = 1001 #потом переопределим

print('цикл В')
while offset < count:
    r = requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id': group_id,
                                                                           'offset':offset}).json()
    response = r['response']
    count = response['count']

    b.extend(response['users'])

    offset = offset + 1000
    print(offset)
    time.sleep(.7)
print('seconde done')

#с помощью множеств получаем тех кто вышел и тех, кто вступил
A = set(a)
B = set(b)

vishli = A - B
vstupili = B - A
print('Вышло пользователей:',len(vishli) ,vishli)
print('Вступило пользователей:',len(vstupili) ,vstupili)
print(vstupili)

# Создаем соединение с нашей базой данных
conn = sqlite3.connect('group_data.sqlite')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО
X = 'FFFFF'
def add_user(X,B,vishli,vstupili):
    c.execute("INSERT INTO 38369814 (old_spisok,new_spisok,subscribe,unsubscribe) VALUES ('%s','%s','%s','%s')"%(A,B,vishli,vstupili))
    conn.commit()

# Не забываем закрыть соединение с базой данных
conn.close()

