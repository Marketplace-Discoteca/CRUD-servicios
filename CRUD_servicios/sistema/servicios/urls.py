from django.urls import path
from . import views
from .views import servicios

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('servicios', views.servicios, name='servicios'),
    path('servicios/crear', views.crear, name='crear'),
    path('servicios/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('servicios/editar/<int:id>',views.editar, name='editar'),
]