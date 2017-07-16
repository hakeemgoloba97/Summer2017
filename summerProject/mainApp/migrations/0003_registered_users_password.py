# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_remove_registered_users_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_users',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]