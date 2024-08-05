from django.db import models

# Create your models here.
class Suscripcion(models.Model):
    usuario= models.EmailField(max_length=100)
    estado= models.BooleanField(default=False)
    
    def __str__(self):
        return self.usuario+" "+str(self.estado)