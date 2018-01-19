# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FerielApp', '0007_communaute_modele_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communaute',
            name='modele_fk',
        ),
        migrations.AddField(
            model_name='communaute',
            name='modele_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Modele'),
        ),
    ]
