from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    marca = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes')
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, max_length=200)
    def __str__(self):
        return self.nombre