# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0015_auto_20171212_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidance',
            name='message',
            field=models.TextField(max_length=200, verbose_name='Mensagem'),
        ),
    ]
