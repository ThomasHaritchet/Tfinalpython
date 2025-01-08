from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),  # Ruta para la página "Acerca de"
    path('', views.blog_list, name='blog_list'),  # Página de lista de blogs
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Detalles de un blog
    path('create/', views.create_blog, name='create_blog'),  # Crear un nuevo blog
    path('<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),  # Editar un blog
    path('logout/', views.logout_view, name='logout'),

]
