"""FerielProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from FerielProject.FerielApp import views as core_views


urlpatterns = [
     url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    url(r'^profile/$', core_views.profile_view, name='profile'),
    url(r'^profile/edit$',core_views.edit_profile, name='edit_profile'),
    url(r'^profile/group/join$',core_views.join_group, name='join_group'),
    url(r'^profile/group/$',core_views.UserGroups, name='usergroups'),
    url(r'^profile/group/(?P<groupid>\d+)/$', core_views.GroupDetails, name='group_details'),
    url(r'^profile/group/delete/(?P<grpid>\d+)$', core_views.DeleteGroup, name='DeleteGroup'),
    url(r'^profile/communities/$', core_views.UserCommunities, name='usercommunities'),
    url(r'^profile/communities/(?P<commid>\d+)$', core_views.CommunityDetails, name='communitydetails'),
    url(r'^profile/communities/join$',core_views.join_community, name='join_community'),
    url(r'^profile/communities/delete/(?P<commid>\d+)$', core_views.DeleteCommunity, name='DeleteCommunity'),
    url(r'^profile/communities/add/$', core_views.AddCommunity, name='AddCommunity'),
    url(r'^profile/communities/Conf_Modele_Community/(?P<commid>\d+)$', core_views.Conf_Modele_Community, name='Conf_Modele_Community'),
    url(r'^profile/communities/Conf_Rubrique_Community/(?P<commid>\d+)$', core_views.Conf_Rubrique_Community, name='Conf_Rubrique_Community'),
    url(r'^profile/communities/Conf_Rubrique_Community/Add_rubrique/(?P<modid>\d+)/(?P<commid>\d+)$', core_views.Add_rubrique, name='Add_rubrique'),
    url(r'^profile/communities/(?P<commid>\d+)/comment/(?P<componentid>\d+)/$', core_views.AddComment, name='AddComment'),
    url(r'^profile/communities/(?P<commid>\d+)/component/$', core_views.AddComponent, name='AddComponent'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/$', core_views.ComponentDetails, name='ComponentDetails'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/deleteCode/(?P<codeid>\d+)/$', core_views.DeleteCode, name='DeleteCode'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/deleteCommit/(?P<commitid>\d+)/$', core_views.DeleteCommit, name='DeleteCommit'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/deleteSujet/(?P<sujetid>\d+)/$', core_views.DeleteSujet, name='DeleteSujet'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/AddCode/$', core_views.AddCode, name='AddCode'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/AddCommit/$', core_views.AddCommit, name='AddCommit'),
    url(r'^profile/communities/(?P<commid>\d+)/(?P<compoid>\d+)/AddSubject/$', core_views.AddSubject, name='AddSubject'),
    url(r'^profile/communities/(?P<commid>\d+)/search_component/$', core_views.SearchComponent, name='SearchComponent'),

    url(r'^profile/reports/$', core_views.All_reports, name='All_reports'),
    url(r'^profile/process/$', core_views.All_process, name='All_process'),
    url(r'^profile/languages/$', core_views.All_languages, name='All_languages'),

    url(r'^profile/languages/Addlng/$', core_views.Add_languages, name='Add_languages'),
    url(r'^profile/reports/Addreport/$', core_views.Add_reports, name='Add_reports'),
    url(r'^profile/process/Addprocess/$', core_views.Add_process, name='Add_process'),

    url(r'^profile/languages/delete/(?P<lngid>\d+)$', core_views.Del_languages, name='Del_languages'),
    url(r'^profile/reports/delete/(?P<reportid>\d+)$', core_views.Del_reports, name='Del_reports'),
    url(r'^profile/process/delete/(?P<processid>\d+)$', core_views.Del_process, name='Del_process'),


    url(r'^profile/languages/Addsyntaxe/(?P<lngid>\d+)/$', core_views.Add_syntaxe, name='Add_syntaxe'),
    url(r'^profile/languages/Addmetam/(?P<lngid>\d+)/$', core_views.Add_meta_m, name='Add_meta_m'),
    url(r'^profile/languages/RatingLanguage/(?P<lngid>\d+)/$', core_views.Rating_language, name='Rating_language'),
    

]

