# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brad', '0003_auto_20170319_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brad.Master'),
        ),
    ]