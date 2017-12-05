# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Heroes', '0003_heroes_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroes',
            name='game',
        ),
        migrations.AddField(
            model_name='heroes',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Heroes.Game'),
        ),
        migrations.RemoveField(
            model_name='heroes',
            name='hero_class',
        ),
        migrations.AddField(
            model_name='heroes',
            name='hero_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Heroes.HeroClass'),
        ),
    ]
