from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('todo/', views.index1),
    path('todo/completed/', views.index2),
]