# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_auto_20171206_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biochemical',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='biochemicalexam',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='value_biochemical', to='patient.Biochemical', verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='patology',
            field=models.ManyToManyField(blank=True, related_name='consultation_patology', to='patient.Patology', verbose_name='Patologia'),
        ),
        migrations.AlterField(
            model_name='foodanalysis',
            name='guidance',
            field=models.ManyToManyField(blank=True, related_name='analysis_guidance', to='patient.Guidance', verbose_name='Orientação'),
        ),
        migrations.AlterField(
            model_name='foodanalysis',
            name='guidanceaux',
            field=models.ManyToManyField(blank=True, related_name='analysis_guidanceaux', to='patient.GuidanceAux', verbose_name='Orientação pré-definida'),
        ),
    ]