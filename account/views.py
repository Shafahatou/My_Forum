from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    
    return render(request, 'myapp/login.html')



def register_view(request):
    if request.method == 'POST':
        User = get_user_model()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                return redirect('index')
            except Exception as e:
                messages.error(request, f"Erreur lors de l'inscription : {e}")
        else:
            messages.error(request, "Les mots de passe ne correspondent pas.")
    
    return render(request, 'myapp/register.html')



def logout_view(request):
    logout(request)
    return redirect('index')