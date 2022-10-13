from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserChangeForm, CostumUserCreationForm
from .models import Comentarios, CostumUser, Noticias

class CostumUserAdmin(UserAdmin):
    auth_form = CostumUserCreationForm
    model = CostumUser
    form = CostumUserChangeForm

class ComentarioInLine(admin.StackedInline):
    model = Comentarios

class NoticiaAdmin(admin.ModelAdmin):
    inlines = [ComentarioInLine]

admin.site.register(CostumUser, CostumUserAdmin)
admin.site.register(Noticias,NoticiaAdmin)
admin.site.register(Comentarios)