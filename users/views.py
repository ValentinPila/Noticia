from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
#from django.contrib.auth.forms import UserCreationForm
from .forms import CostumUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import Noticias
from django.contrib.auth.mixins import LoginRequiredMixin # que afuerzas necesitas ester loggeado a la pagina 
from django.core.exceptions import PermissionDenied


class HomePageView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CostumUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class NoticiasPageView(ListView):
    template_name = 'noticias.html'
    model = Noticias
    context_object_name = 'Todas_Las_Noticias'

class NoticiasPageDetail(DetailView):
    template_name = 'noticias_detalle.html'
    model = Noticias
    context_object_name = 'Noticia_Completa'

class NoticiasPageCreate(LoginRequiredMixin,CreateView):
    template_name = 'noticias_nuevo.html'
    model = Noticias
    fields = "__all__"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class NoticiasPageUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'noticias_editar.html'
    model = Noticias
    fields = "__all__"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class NoticiasPageDelete(LoginRequiredMixin,DeleteView):
    model = Noticias
    success_url = '/'
    template_name = 'noticias_delete.html'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)    