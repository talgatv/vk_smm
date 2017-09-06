# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.CharField(db_index=True, max_length=100, verbose_name='vk_id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('in_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('out_time', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smm.Group')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usergroup',
            unique_together=set([('vk_id', 'group')]),
        ),
    ]
