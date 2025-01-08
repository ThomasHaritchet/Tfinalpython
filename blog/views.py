from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}!')
            return redirect('home')
        messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista de registro
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Vista para mostrar la lista de blogs
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

# Vista para mostrar los detalles de un blog
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

# Vista de "Acerca de"
def about(request):
    return render(request, 'about.html')

# Vista para crear un nuevo blog (solo para usuarios autenticados)
@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El blog se ha creado exitosamente.')
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

# Vista para editar un blog existente (solo para usuarios autenticados)
@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'El blog ha sido actualizado correctamente.')
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})

# Vista para eliminar un blog (solo para usuarios autenticados)
@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    messages.success(request, 'El blog ha sido eliminado correctamente.')
    return redirect('blog_list')

# Vista de logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión con éxito.')
    return redirect('home')  # O la página que desees redirigir después de hacer logout.



