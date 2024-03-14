from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import MensajeContacto
from .forms import MensajeContactoForm

def home(request):
  return render(request, 'inicio/home.html')

def about(request):
  return render(request, 'inicio/about.html')

class MensajeContactoCreateView(CreateView):
    model = MensajeContacto
    form_class = MensajeContactoForm
    template_name = 'inicio/contacto.html'
    success_url = '/contacto/'