# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 21:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_userratings_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userratings',
            name='number',
        ),
    ]