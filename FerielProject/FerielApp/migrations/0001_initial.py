# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-31 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('is_main', models.BooleanField(default=False)),
                ('is_resolved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contexte', models.CharField(blank=True, max_length=30)),
                ('type_cmm', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('objectif', models.CharField(blank=True, max_length=30)),
                ('sequence', models.CharField(blank=True, max_length=200)),
                ('is_resolved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Communaute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('motsCles', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Composant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type_c', models.CharField(blank=True, max_length=30)),
                ('categorie', models.CharField(blank=True, max_length=30)),
                ('lien', models.CharField(blank=True, max_length=300)),
                ('communaute_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Communaute')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('communaute_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Communaute')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MetaModele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('language_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('type_m', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('attributs', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Processus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('sujet', models.CharField(blank=True, max_length=100)),
                ('contexte', models.CharField(blank=True, max_length=30)),
                ('framework', models.CharField(blank=True, max_length=100)),
                ('qualites_attributs', models.CharField(blank=True, max_length=100)),
                ('techniques', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(blank=True, max_length=30)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile_Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Communaute')),
                ('profile_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contexte', models.CharField(blank=True, max_length=30)),
                ('type_r', models.CharField(blank=True, max_length=30)),
                ('id_objectif', models.CharField(blank=True, max_length=30)),
                ('titre_objectif', models.CharField(blank=True, max_length=30)),
                ('vu', models.BooleanField(default=False)),
                ('profile_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('privileges', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('contexte', models.CharField(blank=True, max_length=30)),
                ('sequence', models.CharField(blank=True, max_length=200)),
                ('is_resolved', models.BooleanField(default=False)),
                ('composant_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Composant')),
            ],
        ),
        migrations.CreateModel(
            name='Syntaxe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('language_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Language')),
            ],
        ),
        migrations.AddField(
            model_name='processus',
            name='profile_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile'),
        ),
        migrations.AddField(
            model_name='language',
            name='profile_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='profile_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile'),
        ),
        migrations.AddField(
            model_name='composant',
            name='profile_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile'),
        ),
        migrations.AddField(
            model_name='communaute',
            name='profile_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Profile'),
        ),
        migrations.AddField(
            model_name='commit',
            name='composant_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Composant'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='composant_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Composant'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='discussion_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Discussion'),
        ),
        migrations.AddField(
            model_name='code',
            name='composant_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FerielApp.Composant'),
        ),
    ]