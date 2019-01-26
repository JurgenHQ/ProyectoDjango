from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.
#Vista para el inicio
def inicio(request):
    titulo = "Hola usuario no logueado"
    if request.user.is_authenticated: #verifica si el usuario esta logeado
        titulo = " Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    context ={
        "titulo":titulo,
        "form": form,
    }
    if form.is_valid(): #confirma si es valido el formulario
        instance = form.save(commit = False)
        form_data=form.cleaned_data #obtiene los datos limpios del formulario
        correo = form_data.get("email") #obtiene el email
        nomb = form.cleaned_data.get("nombre") #obtiene el nombre
        if not instance.nombre:
            instance.nombre= "User"
        instance.save()
        context ={
            "titulo": "Gracias %s!" %(nomb)
        }
        if not nomb:
            context={
                "titulo":"Gracias User"
            }

    return render(request, "base.html", context)
#Vista para el Contacto

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_nombre = form.cleaned_data.get("nombre")
        form_asunto = form.cleaned_data.get("asunto")
        form_mensaje = form.cleaned_data.get("mensaje")
        email_from = settings.EMAIL_HOST_USER
        email_to = ["jurgenhuerlo25@gmail.com","jurgen.huerlo@pucese.edu.ec"]
        email_mensaje = "%s:\n %s \n\nEnviador por:  %s " %(form_nombre,form_mensaje,form_email)
        asunto=form_asunto
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently = True
        )


    context={
        "contact_form": form
    }
    return render(request, "contact.html", context)

def about(request):
    
    titulo="Acerca de Nosotros"

    context={
        "titulo_about":titulo
    }

    return render(request, "about.html", context)