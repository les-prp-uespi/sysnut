# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20171118_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='patology',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultation_patology', to='patient.Patology', verbose_name='Patologia'),
        ),
    ]
