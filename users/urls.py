from django.urls import path 

from .views import *

urlpatterns = [
    path('noticias/', NoticiasPageView.as_view(), name='noticia'),
    path('noticias/<int:pk>/', NoticiasPageDetail.as_view(), name='noticias_detalle'),
    path('noticias/nuevo/', NoticiasPageCreate.as_view(), name='noticias_nuevo'),
    path('noticias/<int:pk>/Editar', NoticiasPageUpdate.as_view(), name='noticias_editar'),
    path('noticias/<int:pk>/delete', NoticiasPageDelete.as_view(), name='noticias_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]
