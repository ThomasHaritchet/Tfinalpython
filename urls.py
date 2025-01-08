from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Vista principal de la página de inicio
def home(request):
    return render(request, 'home.html')  # Renderiza el archivo 'home.html'

# Vista para la sección "Acerca de mí"
def about(request):
    return render(request, 'about.html')  # Renderiza el archivo 'about.html'

# Rutas URL del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta al panel de administración de Django
    path('blogs/', include('blog.urls')),  # Incluir rutas de la app 'blog'
    path('', home, name='home'),  # Ruta a la página de inicio
    path('about/', about, name='about'),  # Ruta a la página "Acerca de mí"
    path('accounts/', include('perfiles.urls')),
    path('messages/', include('mensajes.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

