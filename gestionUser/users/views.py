from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Vista para el login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

# Vista para el logout
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

# Vista para el home con permisos
@login_required
def home(request):
    user = request.user
    context = {
        'can_view_ventas': user.has_perm('users.view_ventas'),
        'can_view_compras': user.has_perm('users.view_compras'),
        'can_view_inventarios': user.has_perm('users.view_inventarios'),
    }
    return render(request, 'home.html', context)  # Aquí falta el render para mostrar el home

# Vista para manejar el error 404
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
