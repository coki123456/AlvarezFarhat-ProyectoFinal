from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    email     = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}


class FormularioCambiarContraseña(PasswordChangeForm):

    old_password  = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}

class FormularioEditarPerfil(forms.Form):   
    email       = forms.EmailField(required=True, widget=forms.EmailInput())
    nombre      = forms.CharField(required=False, widget=forms.TextInput())
    apellido    = forms.CharField(required=False, widget=forms.TextInput())
    descripcion = forms.CharField(max_length=200, required=False, widget=forms.Textarea())
    link        = forms.URLField(max_length=100, required=False, widget=forms.TextInput())
    avatar      = forms.ImageField(required=False, widget=forms.ClearableFileInput())
