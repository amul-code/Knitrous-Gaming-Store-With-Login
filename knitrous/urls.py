from django.contrib import admin
from django.urls import path ,include
from knitrous import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("games",views.games,name='games'),
    path("accessories",views.accessories,name='accessories'),
    path("es",views.es,name='es'),
    path("clan",views.clan,name='clan'),
    path("login", views.login, name='login'),
]