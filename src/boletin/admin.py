from django.contrib import admin

# Register your models here.
from .models import Registrado
from .forms import RegModelForm

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timeestamp"]
    form = RegModelForm
    list_filter = ["timeestamp"]
    list_editable = ["nombre"]
    search_fields =["email","nombre"]


admin.site.register(Registrado, AdminRegistrado)