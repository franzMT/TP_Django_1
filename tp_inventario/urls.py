from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',views.ListadoProductos,name='listado'),
    path('crear/',views.CrearProducto,name='crear'),
    path('eliminar/<id_producto>',views.EliminarProducto,name='eliminar'),
    path('editar/<id_producto>',views.EditarProducto,name='editar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
