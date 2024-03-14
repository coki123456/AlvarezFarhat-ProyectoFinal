from django.urls import path
from .views import home, about, MensajeContactoCreateView

urlpatterns = [
    path('', home, name = 'home' ),
    path('about/', about, name = 'about' ),
    path('contacto/', MensajeContactoCreateView.as_view(), name = 'contacto' ),
    
]