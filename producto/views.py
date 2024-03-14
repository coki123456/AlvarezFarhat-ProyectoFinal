from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/listar_producto.html'
    context_object_name = 'productos'
    paginate_by = 50
    
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm   
    template_name = 'producto/crear_producto.html'
    success_url = '/producto/'
    
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'producto/crear_categoria.html'
    success_url = '/producto/'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/editar_producto.html'
    success_url = '/producto/'

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'producto/eliminar_producto.html'
    success_url = '/producto/'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto/ver_producto.html'
    context_object_name = 'objeto'
    
    
    
