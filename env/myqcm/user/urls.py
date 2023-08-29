from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.connexion,name='login'),
    path('logout',views.deconnection,name='logout'),
    path('acceuil',views.acceuil,name='acceuil'),

]