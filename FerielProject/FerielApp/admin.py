from django.contrib import admin
from FerielProject.FerielApp.models import Rubrique,Photo,Profile,Modele,Role,Commentaire,Discussion,Sujet,Commit,Code,Groupe,Composant,Communaute,Processus,Syntaxe,MetaModele,Language,Rapport,Profile_Community

# Show models on backend
admin.site.register(Profile)
admin.site.register(Modele)
admin.site.register(Groupe)
admin.site.register(Commentaire)
admin.site.register(Discussion)
admin.site.register(Sujet)
admin.site.register(Commit)
admin.site.register(Code)
admin.site.register(Composant)
admin.site.register(Communaute)
admin.site.register(Processus)
admin.site.register(Syntaxe)
admin.site.register(MetaModele)
admin.site.register(Language)
admin.site.register(Rapport)
admin.site.register(Profile_Community)
admin.site.register(Role)
admin.site.register(Photo)
admin.site.register(Rubrique)



