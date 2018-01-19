from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Profile






class EditProfileForm(forms.ModelForm):

    username =  forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'id': 'username',
                                                                  'name': 'username'})) 
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'id': 'first_name',
                                                                  'name': 'first_name'}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'id': 'last_name',
                                                                  'name': 'last_name'})) 
    email = forms.EmailField(max_length=254,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': 'email',
                                                            'name': 'email'}))
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
    #                                                               'id': 'password1',
    #                                                               'name': 'password'}))


    # password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'class': 'form-control',
    #                                                           'id': 'password',
    #                                                           'name': 'password'}))
    

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']



class SignUpForm(UserCreationForm):
    
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'id': 'username',
                                                                  'name': 'username'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': 'email',
                                                            'name': 'email'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': 'password1',
                                                                  'name': 'password'}))


    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                              'id': 'password',
                                                              'name': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        