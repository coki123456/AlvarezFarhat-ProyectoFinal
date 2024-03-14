from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoDeleteView, ProductoUpdateView, CategoriaCreateView, ProductoDetailView

urlpatterns = [
    path('', ProductoListView.as_view(), name = 'listar_producto' ),
    path('crear_producto/', ProductoCreateView.as_view(), name = 'crear_producto' ),
    path('crear_categoria/', CategoriaCreateView.as_view(), name = 'crear_categoria' ),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name = 'editar_producto' ),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name = 'eliminar_producto' ),
    path('<int:pk>/detalle/', ProductoDetailView.as_view(), name='ver_producto'),
]