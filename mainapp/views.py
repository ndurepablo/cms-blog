from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        "title": "Home",
    })
def about(request):
    return render(request, 'mainapp/about.html', {
        "title": "About",
    })
    
def register_page(request):
    register_form = RegisterForm()
    
    # Recibe el método en mediante el form
    if request.method == "POST":
        # envia la rq mediante POST
        register_form = RegisterForm(request.POST)
        # si el formulario es válido
        if register_form.is_valid():
            # guarda el registro
            register_form.save()
            # redirecciona a la página de inicio
            return redirect('index')
            
    
    return render(request, "users/register.html", {
        "title": "Registro",
        "register_form": register_form,
    })