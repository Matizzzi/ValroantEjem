from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import requests

def comprar(request):
    carro = request.session.get("carro", [])
    total = 0
    for item in carro: 
        total += item[5]
    
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()

    # Crear los detalles de la venta
    for item in carro:
        detalle = DetalleVenta(
            venta=venta,
            producto=Producto.objects.get(codigo=item[0]),
            cantidad=item[4],
            precio=item[3]
        )
        detalle.save()
    
    request.session["carro"] = []  # Limpiar el carrito después de la compra
    return redirect(to="carrito")

def carrito(request):
    carro = request.session.get("carro", [])
    productos = []
    for item in carro:
        producto = Producto.objects.get(codigo=item[0])
        productos.append({
            'codigo': producto.codigo,
            'nombre': producto.detalle,
            'imagen': producto.imagen,
            'precio': producto.precio,
            'cantidad': item[4],
            'subtotal': item[5]
        })
    
    total = sum(item[5] for item in carro)
    return render(request, 'core/carrito.html', {'productos': productos, 'total': total})





def home(request):
    context = {}  # Inicializa el diccionario context
    suscrito(request, context)
    return render(request, 'core/index.html', context)
def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        try:
            response = requests.get(f"http://127.0.0.1:8000/api/suscribir/{email}")
            response.raise_for_status()
            data = response.json()
            print(data)  # Verifica el contenido de la respuesta
            context["suscrito"] = data.get("suscrito", False)
        except requests.RequestException as e:
            context["suscrito"] = False
            print(f"Error al hacer la solicitud: {e}")


def productos(request):
    productos_en_venta = Producto.objects.all()  # Usa el modelo Producto aquí
    return render(request, 'core/producto.html', {'productos_en_venta': productos_en_venta, "carro":request.session.get("carro", [])})


def mapass(request):
    return render(request, 'core/mapa.html')

def agentes(request):
    return render(request, 'core/agente.html')

def arsena(request):
    return render(request, 'core/arsenal.html')

def pagars(request):
    return render(request, 'core/pagar.html')

def registros(request):
    return render(request, 'core/registro.html')

def loogin(request):
    return render(request, 'core/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Registro()
    
    return render(request, 'core/registro.html', {'form': form})

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    
    for item in carro:
        if item[0] == codigo:
            item[4] += 1  # Incrementar cantidad
            item[5] = item[3] * item[4]  # Actualizar subtotal
            break
    else:
        carro.append([
            codigo, 
            producto.detalle, 
            producto.imagen, 
            producto.precio, 
            1,  # Cantidad
            producto.precio  # Subtotal
        ])
    
    request.session["carro"] = carro
    return redirect(to="productos")


def limpiar(request):
    request.session.flush()
    return redirect(to="productos")