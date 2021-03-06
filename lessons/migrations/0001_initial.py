# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('time_starting', models.TimeField(verbose_name='time starting')),
                ('time_ending', models.TimeField(verbose_name='time ending')),
                ('weekday', models.IntegerField(choices=[('monday', 0), ('tuesday', 1), ('wednesday', 2), ('thursday', 3), ('friday', 4), ('saturday', 5), ('sunday', 6)], default=0, verbose_name='weekday')),
                ('max_attendance', models.IntegerField(default=10, verbose_name='max. attendance')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('students', models.ManyToManyField(to='students.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
