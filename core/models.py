from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Importa timezone

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)  # Cambia aquí
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.cliente.username + " " + str(self.fecha)

class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=400)
    
    def tachado(self):
        if self.oferta:
            return "$" + str(round(self.precio * 1.2))
        return ""
    
    def __str__(self):
        return self.detalle + "(" + self.codigo + ")"

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return str(self.id) + " " + self.producto.detalle[0:12] + " " + str(self.venta.id)
