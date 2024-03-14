from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre + " - " +  self.email + " - " + self.mensaje[:25] + "..."
