from django import forms
from .models import Registrado

#formulario de registro con el modelo
class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado #variable que obtendra los metodos de la clase Registrado
        fields= ["nombre","email"] #los parametros que se le van a pasar

#formulario de contacto customizado

class ContactForm(forms.Form): # crea un formulario
    nombre = forms.CharField(max_length=100) #los atributos o entradas que tendra el formulario
    email = forms.EmailField()
    asunto = forms.CharField()
    mensaje = forms.CharField(widget = forms.Textarea)