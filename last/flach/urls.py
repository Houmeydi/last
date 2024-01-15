from django.urls import path
from . import views
app_name="flach"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:livre_id>/', views.show, name="show"),
    path('ajouter_livre/ ',views.add, name="add"),
    path('supprimer_livre/,<int:livre_id>/', views.delete, name="delete"),
    path('modifie_livre/, <int:livre_id>/', views.modifie, name="modifie"),
]
