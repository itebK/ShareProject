from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.template import RequestContext


from FerielProject.FerielApp.models import Profile, Modele, Groupe, Role, Communaute, Discussion, Composant, Commentaire, Sujet, Commit, Code, Processus, Language, Syntaxe, MetaModele, Rapport, Profile_Community,Rubrique
from FerielProject.FerielApp.forms import SignUpForm, EditProfileForm
from FerielProject.FerielApp.tokens import account_activation_token


@login_required
def home(request):
    all_groups = Group.objects.all()
    all_communities = Communaute.objects.all()
    my_p = Profile.objects.get(user=request.user)
    
    return render(request, 'home.html', {"all_groups": all_groups, "all_communities": all_communities,"my_p":my_p})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, initial={
                           'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
    if request.method == 'POST':
        if form.is_valid():
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            # user.set_password(request.POST['password'])

            user.save()
            return HttpResponseRedirect('%s' % (reverse('profile')))

    context = {
        "form": form
    }

    return render(request, "edit_profile.html", context)


def profile_view(request):
    user = request.user
    form = EditProfileForm(initial={
                           'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name})

    context = {
        "form": form,

    }
    return render(request, 'profile.html', context)


def join_group(request):
    idgrp = request.GET.get('id')

    group = Group.objects.get(id=idgrp)
    request.user.groups.add(group)
    return HttpResponseRedirect('/')


def UserGroups(request):
    userGroups = request.user.groups.all()

    #userGroups = Groupe.objects.filter(id__in=request.user.id).select_related("group")

    return render(request, 'groups.html', {"UserGroups": userGroups})


def GroupDetails(request, groupid):

    group_details = request.user.groups.filter(pk=groupid)
    group_members = User.objects.filter(groups__id=groupid)
    return render(request, 'group_details.html', {"group_details": group_details, "group_members": group_members})


def DeleteGroup(request, grpid):
    x = Group.objects.filter(id=grpid).delete()
    return redirect('../../group')


def UserCommunities(request):
    communities_id = Profile_Community.objects.filter(
        profile_fk__id=request.user.id).values_list('community_fk', flat=True)
    
    communities = Communaute.objects.filter(
        id__in=communities_id).select_related("profile_fk")
    
    

    return render(request, 'communities.html', {"communities": communities})


def CommunityDetails(request, commid):
    community_details = Communaute.objects.filter(id=commid)
    profile_community = Profile_Community.objects.filter(
        community_fk__id=commid)
    get_all_component = Composant.objects.filter(communaute_fk__id=commid)
    get_all_comments = Commentaire.objects.all().order_by('-comment_date')



    models = []
    #print commid
    get_rubriques = Rubrique.objects.all()
    get_comm = Communaute.objects.filter(id=commid).values('modele_fk')
    for m in get_comm:
        #print m['modele_fk']
        get_modele = Modele.objects.filter(id=m['modele_fk']).values('id','rubrique_fk','libelle','description','type_m')
        models.append(get_modele)
        #print get_modele
    #print models

    return render(request, 'community_details.html', {"community_details": community_details, "profile_community": profile_community, "get_all_component": get_all_component, "get_all_comments": get_all_comments,"models":models,"get_rubriques":get_rubriques,"commid":commid})


def join_community(request):
    idcomm = request.GET.get('id')
    communaute = Communaute.objects.get(id=idcomm)
    my_p = Profile.objects.get(user=request.user)
    commQuery = Profile_Community(profile_fk=my_p, community_fk=communaute)
    commQuery.save()
    return HttpResponseRedirect('/')


def DeleteCommunity(request, commid):
    x = Profile_Community.objects.filter(
        profile_fk__id=request.user.id, community_fk__id=commid).delete()
    return redirect('../../communities')


def AddComment(request, componentid, commid):

    commentcont = request.POST.get("commentcontent" + componentid, False)
    my_p = Profile.objects.get(user=request.user)
    my_component = Composant.objects.get(id=componentid)
    add_comment = Commentaire(
        profile_fk=my_p, composant_fk=my_component, contexte=commentcont)
    add_comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def AddComponent(request, commid):
    models=[]
    get_mod_community = Communaute.objects.filter(id=commid).values("modele_fk")
    for gmc in get_mod_community : 
        print gmc['modele_fk']
        get_mod = Modele.objects.get(id=gmc['modele_fk'])
        print get_mod
        models.append(get_mod)
    #print get_mod_community
    #get_models = Modele.objects.filter()
    if request.method == 'POST':
        modele_input = request.POST.get("modele", False)
        modele = Modele.objects.filter(libelle=modele_input).first()
        my_p = Profile.objects.get(user=request.user)
        community = Communaute.objects.get(id=commid)
        libelle = request.POST.get("libelle", False)
        description = request.POST.get("description", False)
        typec = request.POST.get("typec", False)
        categorie = request.POST.get("categorie", False)
        lien = request.POST.get("lien", False)
        compo = Composant(libelle=libelle, description=description, type_c=typec, categorie=categorie,
                          lien=lien, profile_fk=my_p, communaute_fk=community, modele_fk=modele)

        if (compo.libelle != False):
            compo.save()
            return redirect('/profile/communities/' + commid)

    return render(request, 'components.html',{"models":models})


def ComponentDetails(request, commid, compoid):
    codes = Code.objects.filter(composant_fk=compoid)
    commits = Commit.objects.filter(composant_fk=compoid)
    sujets = Sujet.objects.filter(composant_fk=compoid)
    return render(request, 'components_details.html', {"codes": codes, "commits": commits, "sujets": sujets, "commitid": commid, "componentid": compoid})


def DeleteCode(request, commid, compoid, codeid):
    Code.objects.filter(id=codeid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def DeleteCommit(request, commid, compoid, commitid):
    print commitid
    Commit.objects.filter(id=commitid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def DeleteSujet(request, commid, compoid, sujetid):
    Sujet.objects.filter(id=sujetid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def AddCode(request, commid, compoid):
    if request.method == 'POST':
        component = Composant.objects.filter(id=compoid).first()
        libelle = request.POST.get("libelle", False)
        isresolved = request.POST.get("isresolved", False)
        ismain = request.POST.get("ismain", False)
        if isresolved == '':
            isresolved = True
        if ismain == '':
            ismain = True
        code = Code(libelle=libelle, is_main=ismain,
                    is_resolved=isresolved, composant_fk=component)
        code.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def AddCommit(request, commid, compoid):
    if request.method == 'POST':
        component = Composant.objects.filter(id=compoid).first()
        libelle = request.POST.get("libelle", False)
        isresolved = request.POST.get("isresolved", False)
        goals = request.POST.get("goals", False)
        sequence = request.POST.get("sequence", False)
        if isresolved == '':
            isresolved = True

        commit = Commit(libelle=libelle, is_resolved=isresolved,
                        composant_fk=component, objectif=goals, sequence=sequence)
        commit.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def AddSubject(request, commid, compoid):
    if request.method == 'POST':
        component = Composant.objects.filter(id=compoid).first()
        libelle = request.POST.get("libelle", False)
        isresolved = request.POST.get("isresolved", False)
        contexte = request.POST.get("context", False)
        sequence = request.POST.get("sequence", False)
        if isresolved == '':
            isresolved = True

        sujet = Sujet(libelle=libelle, is_resolved=isresolved,
                      composant_fk=component, contexte=contexte, sequence=sequence)
        sujet.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def All_reports(request):
    my_p = Profile.objects.get(user=request.user)
    reports = Rapport.objects.filter(profile_fk=my_p)
    return render(request, 'reports.html', {"reports": reports})


def All_languages(request):
    my_p = Profile.objects.get(user=request.user)
    languages = Language.objects.filter(profile_fk=my_p)
    syntaxe = Syntaxe.objects.all()
    meta_m = MetaModele.objects.all()
    return render(request, 'language.html', {"languages": languages, "syntaxe": syntaxe, "meta_m": meta_m})


def All_process(request):
    my_p = Profile.objects.get(user=request.user)
    process = Processus.objects.filter(profile_fk=my_p)
    return render(request, 'process.html', {"process": process})


def Add_reports(request):
    if request.method == 'POST':
        my_p = Profile.objects.get(user=request.user)
        contexte = request.POST.get("context", False)
        type_r = request.POST.get("type_r", False)
        id_objectif = request.POST.get("id_objectif", False)
        titre_objectif = request.POST.get("titre_objectif", False)
        vu = request.POST.get("vu", False)
        if vu == '':
            vu = True
        report = Rapport(contexte=contexte, profile_fk=my_p,type_r=type_r,id_objectif=id_objectif,titre_objectif=titre_objectif,vu=vu)
        report.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Add_languages(request):
    if request.method == 'POST':
        my_p = Profile.objects.get(user=request.user)
        libelle = request.POST.get("libelle", False)
        language = Language(libelle=libelle, profile_fk=my_p)
        language.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Add_process(request):
    if request.method == 'POST':
        my_p = Profile.objects.get(user=request.user)
        libelle = request.POST.get("libelle", False)
        sujet = request.POST.get("sujet", False)
        contexte = request.POST.get("contexte", False)
        framework = request.POST.get("framework", False)
        qualites_attributs = request.POST.get("qualites_attributs", False)
        techniques = request.POST.get("techniques", False)
    
        process = Processus(profile_fk=my_p,libelle=libelle,sujet=sujet,contexte=contexte,framework=framework,qualites_attributs=qualites_attributs,techniques=techniques)
        process.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Del_languages(request, lngid):
    Language.objects.filter(id=lngid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Del_reports(request, reportid):
    Rapport.objects.filter(id=reportid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Del_process(request, processid):
    Processus.objects.filter(id=processid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Add_syntaxe(request, lngid):
    if request.method == 'POST':
        language_fk = Language.objects.get(id=lngid)
        libelle = request.POST.get("libelle", False)
        description = request.POST.get("description", False)
        syntaxe = Syntaxe(
            libelle=libelle, language_fk=language_fk, description=description)
        if libelle != False:
            syntaxe.save()
            return redirect('/profile/languages/')
    return render(request, 'syntaxe.html')


def Add_meta_m(request, lngid):
    if request.method == 'POST':
        language_fk = Language.objects.get(id=lngid)
        libelle = request.POST.get("libelle", False)
        description = request.POST.get("description", False)
        meta_m = MetaModele(
            libelle=libelle, language_fk=language_fk, description=description)
        if libelle != False:
            meta_m.save()
            return redirect('/profile/languages/')
    return render(request, 'meta_m.html')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def SearchComponent(request, commid):
    if request.method == 'POST':
        libelle = request.POST.get('search_component')
        community_details = Communaute.objects.filter(id=commid)
        profile_community = Profile_Community.objects.filter(
        community_fk__id=commid)
        get_all_component_search = Composant.objects.filter(communaute_fk__id=commid,libelle__contains = libelle)
        get_all_comments = Commentaire.objects.all().order_by('-comment_date')

    return render(request, 'search_component.html', {"profile_community": profile_community,"community_details":community_details,"get_all_component_search":get_all_component_search,"get_all_comments":get_all_comments})



def Rating_language(request,lngid):
    
    etoile = request.POST.get('starsnumbers')
    language = Language.objects.get(id=lngid)
    print language
    language.etoile = etoile 
    language.save() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def AddCommunity(request):
    #all_modele = Modele.objects.all()
    if request.method == 'POST':
            # modele_input = request.POST.get("modele", False)
            # modele = Modele.objects.filter(libelle=modele_input).first()
            my_p = Profile.objects.get(user=request.user)
            titre = request.POST.get("titre", False)
            description = request.POST.get("description", False)
            motscles = request.POST.get("motscles", False)
            community = Communaute(titre=titre, description=description, motsCles=motscles, profile_fk=my_p) #modele_fk=modele)

    if (community.titre != False):
            community.save()
            
            Profile_Community(profile_fk=my_p,community_fk=community).save()
            return redirect('/profile/communities/Conf_Modele_Community/'+str(community.id))
    return render(request, 'community_add.html')

def Conf_Modele_Community(request,commid):
    all_modele = Modele.objects.all()
    communityid =commid
    i=0
    if request.method == 'POST':
        get_com = Communaute.objects.get(id=commid)
        for mod in all_modele:
            check_mod = request.POST.get(str(mod.id))
            if(check_mod=="on"):
                i+=1
                get_modele =Modele.objects.get(id=mod.id)
                get_com.modele_fk.add(get_modele)
        if i != 0:
            
            return redirect('/profile/communities/Conf_Rubrique_Community/'+commid)
         
    return render(request, 'community_conf_modele.html',{"all_modele":all_modele,"commid":communityid})


def Conf_Rubrique_Community(request,commid):
    models = []
    #print commid
    get_rubriques = Rubrique.objects.all()
    get_comm = Communaute.objects.filter(id=commid).values('modele_fk')
    for m in get_comm:
        #print m['modele_fk']
        get_modele = Modele.objects.filter(id=m['modele_fk']).values('id','rubrique_fk','libelle','description','type_m')
        models.append(get_modele)
        #print get_modele
    #print models
   
    return render(request, 'community_conf_rubr.html',{"models":models,"get_rubriques":get_rubriques,"commid":commid})

def Add_rubrique(request,modid,commid):
    get_modele= Modele.objects.get(id=modid)
    if request.method=="POST" :
        libelle = request.POST.get("libelle", False)
        categorie = request.POST.get("categorie", False)
        type_r = request.POST.get("type_r", False)
        obligatoire = request.POST.get("obligatoire",False)
        if obligatoire == 'on':
            obligatoire=True
        r = Rubrique(libelle=libelle,categorie=categorie,type_r=type_r,obligatoire=obligatoire)
        r.save()
        get_modele.rubrique_fk.add(r)
        if libelle!= '':
            return redirect('/profile/communities/Conf_Rubrique_Community/'+commid)
    return render(request, 'add_rubrique.html')