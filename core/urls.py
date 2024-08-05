from django.urls import path
from .views import *    
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home"),
    path('producto/', productos, name='productos'),
    path('mapa/', mapass, name='mapass'),
    path('agente/', agentes, name='agentes'),
    path('arsenal/', arsena, name='arsena'),
    path('pagar/', pagars, name='pagars'),
    path('carrito', carrito, name='carrito'),
    path('limpiar', limpiar),
    path('comprar', comprar, name="comprar"),
    path('registro/', registro, name='registro'),  # Cambiado para usar la vista `registro`
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('addtocar/<codigo>', addtocar, name='addtocar'),
    
]
