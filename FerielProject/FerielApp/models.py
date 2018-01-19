from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Photo(models.Model):
    photo_profile = models.FileField(upload_to='images', verbose_name='Photos')

    def __str__(self):              # __unicode__ on Python 2
        return str(self.photo_profile)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_fk = models.ForeignKey(
        Photo, blank=True, null=True, on_delete=models.CASCADE)
    sexe = models.CharField(max_length=30, blank=True)
    email_confirmed = models.BooleanField(default=False)
    
    def __str__(self):              # __unicode__ on Python 2
        return str(self.user)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Groupe(Group):
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)

class Rubrique (models.Model):
    
    categorie = models.CharField(max_length=30, blank=True)
    libelle = models.CharField(max_length=30, blank=True)
    type_r = models.CharField(max_length=30, blank=True)
    obligatoire = models.BooleanField(default=False)
 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)


class Modele(models.Model):
    rubrique_fk = models.ManyToManyField(Rubrique,blank=True)
    libelle = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=200, blank=True)
    type_m = models.CharField(max_length=256, choices=[('Conceptual component model','Conceptual component model'),('Software component model','Software component model')])

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)


class Role(models.Model):
    libelle = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=200, blank=True)
    privileges = models.CharField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)

class Communaute(models.Model):
    modele_fk = models.ManyToManyField(Modele)
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    
    titre = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=200, blank=True)
    motsCles = models.CharField(max_length=30, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.titre)


class Discussion(models.Model):
    communaute_fk = models.ForeignKey(
        Communaute, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)




class Composant(models.Model):
    modele_fk = models.ForeignKey(
        Modele, blank=True, null=True, on_delete=models.CASCADE)
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
   
    communaute_fk = models.ForeignKey(
        Communaute, blank=True, null=True, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=200, blank=True)
    type_c = models.CharField(max_length=30, blank=True)
    categorie = models.CharField(max_length=30, blank=True)
    lien = models.CharField(max_length=300, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)




class Commentaire(models.Model):
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    discussion_fk = models.ForeignKey(
        Discussion, blank=True, null=True, on_delete=models.CASCADE)
    composant_fk = models.ForeignKey(
        Composant, blank=True, null=True, on_delete=models.CASCADE)
    contexte = models.CharField(max_length=300, blank=True)
    type_cmm = models.CharField(max_length=200, blank=True)
    comment_date = models.DateTimeField(default=timezone.now, blank=True)


    def __str__(self):              # __unicode__ on Python 2
        return str(self.contexte)




class Sujet(models.Model):
    composant_fk = models.ForeignKey(
        Composant, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    contexte = models.CharField(max_length=30, blank=True)
    sequence = models.CharField(max_length=200, blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)


class Commit(models.Model):
    composant_fk = models.ForeignKey(
        Composant, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    objectif = models.CharField(max_length=30, blank=True)
    sequence = models.CharField(max_length=200, blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)


class Code(models.Model):
    composant_fk = models.ForeignKey(
        Composant, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    is_main = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)





class Processus(models.Model):
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    sujet = models.CharField(max_length=100, blank=True)
    contexte = models.CharField(max_length=30, blank=True)
    framework = models.CharField(max_length=100, blank=True)
    qualites_attributs = models.CharField(max_length=100, blank=True)
    techniques = models.CharField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)

class Language(models.Model):
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    etoile = models.CharField(max_length=10, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)

class Syntaxe(models.Model):
    language_fk = models.ForeignKey(
        Language, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)


class MetaModele(models.Model):
    language_fk = models.ForeignKey(
        Language, blank=True, null=True, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.libelle)





class Rapport(models.Model):
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    contexte = models.CharField(max_length=30, blank=True)
    type_r = models.CharField(max_length=30, blank=True)
    id_objectif = models.CharField(max_length=30, blank=True)
    titre_objectif = models.CharField(max_length=30, blank=True)
    vu = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.contexte)




class Profile_Community(models.Model):
    profile_fk = models.ForeignKey(
        Profile, blank=True, null=True, on_delete=models.CASCADE)
    community_fk = models.ForeignKey(
        Communaute, blank=True, null=True, on_delete=models.CASCADE)
 

    def __str__(self):              # __unicode__ on Python 2
        return str(self.profile_fk)




