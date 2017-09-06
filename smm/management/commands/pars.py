import requests
import csv
import time
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from smm.models import *
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Migrate'


    print ('**************Effects******************')
#тут начинается цикл команды manage.py
    def handle(self, *args, **options):
#позже изменю на не постоянную
        group_id = 3
        offset = 0
        count = 1001 #потом переопределим


        old_users = [] # первая отсечка
        a = [] # вторая отсечка
        new_users = [] # вторая отсечка

        # переделываем переменную в тип который берет id из таблицы group , т.е. 2 это 38369814 , это для того что бы связи внизу работали
        group = Group.objects.filter(id=group_id)[0]

        print('цикл А')
#объект old_users переделывает в список из таблицы UserGroup с фильтром только group_id=2
        old_users = UserGroup.objects.filter(group_id=group.id,out_time=None).values_list('vk_id', flat=True)
        print(group.vk_groip_id)
# начинается цикл обращения к вк
        while offset < count:
            r = requests.get('https://api.vk.com/method/groups.getMembers',
            params={'group_id': group.vk_groip_id, 'offset':offset}).json()
# парсер json ответа
            response = r['response']
            count = response['count']
# цикл который обрабатывет json ответ с параметром users
            for user in response['users']:

# говориткакие столбцы таблицы UserGroup заполнять
                vk_users = UserGroup(
                    vk_id = user,
                    group = group,
                    name = 'user' #по умолчанию в поле name параметр user

                )

# сохраняет всё столбцы в таблицу и если выдаёт ошибку "IntegrityError" что означает что запись уже есть в таблице, то пичатает рядом скип и невносит в таблицу
                try:
                    vk_users.save()
                    print (vk_users.vk_id)
                    new_users.append(vk_users.vk_id)
                except IntegrityError:
                    print(str(vk_users.vk_id) +' -skip')
                    a.append(vk_users.vk_id)


            offset = offset + 1000
            print(offset)
            time.sleep(0.37)
        print('first done')

#объект new_users переделывает в список из таблицы UserGroup с фильтром только group_id=2 ,
        new_users = UserGroup.objects.filter(group_id=group.id).values_list('vk_id', flat=True)
        print('new_users ',len(new_users))
        print('как было, old_users ',len(old_users))
        print('на данный момент, a ',len(a))


        A = set(a)
        B = set(old_users)

        vishli = list(A - B)
        vstupili = list(B - A)
        print('Вышло пользователей:',len(vishli) )
        print('Вступило пользователей:',len(vstupili) )
        # print(vstupili)


        # old_users = a





# выводит что все нормально
        self.stdout.write(self.style.SUCCESS('Successfully ' ))


#
# if __name__ == '__main__':
#     categories()
