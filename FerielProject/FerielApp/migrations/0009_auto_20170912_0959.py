# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FerielApp', '0008_auto_20170912_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(blank=True, max_length=30)),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('type_r', models.CharField(blank=True, max_length=30)),
                ('obligatoire', models.BooleanField(default=False)),
                ('modele_fk', models.ManyToManyField(to='FerielApp.Modele')),
            ],
        ),
        migrations.RemoveField(
            model_name='communaute',
            name='modele_fk',
        ),
        migrations.AddField(
            model_name='communaute',
            name='modele_fk',
            field=models.ManyToManyField(to='FerielApp.Modele'),
        ),
    ]