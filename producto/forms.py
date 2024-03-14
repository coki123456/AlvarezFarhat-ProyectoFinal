from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:500px; height: 45px;'}))
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad', 'marca', 'proveedor', 'categoria', 'imagen', 'descripcion']
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']