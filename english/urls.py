from django.contrib import admin
from django.urls import path,include
from english import  views
urlpatterns = [
    path('',views.english,name="english"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
]
