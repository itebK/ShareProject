# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FerielApp', '0011_auto_20170912_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modele',
            name='rubrique_fk',
            field=models.ManyToManyField(blank=True, to='FerielApp.Rubrique'),
        ),
    ]
