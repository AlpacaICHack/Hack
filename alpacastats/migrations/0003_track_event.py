# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpacastats', '0002_auto_20160220_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alpacastats.Event'),
        ),
    ]
