# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-07 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FerielApp', '0004_commentaire_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='etoile',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='contexte',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
