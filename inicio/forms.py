from django import forms
from .models import MensajeContacto

class MensajeContactoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.EmailInput(attrs={'style': 'width:500px; place-items: center;'})) 
    email = forms.CharField(widget=forms.EmailInput(attrs={'style': 'width:500px; place-items: center;'})) 
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:500px; height: 100px;place-items: center;'}))
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'mensaje']
