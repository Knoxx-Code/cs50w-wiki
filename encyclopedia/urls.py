from django.contrib import admin
from django.urls import path,include

from . import views

from wiki import views as v

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",v.title,name="title"),
    path("search",views.search,name="search"),
    path("create_page",views.create_page,name="create_page"),
    path("wiki/<str:title>/edit_page",views.edit_page,name="edit_page"),
    path("random_page",views.random_page,name="random_page"),

]
