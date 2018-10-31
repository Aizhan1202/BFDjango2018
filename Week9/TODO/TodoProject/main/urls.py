from django.conf.urls import url
from django.urls import path
from . import views
from .views import Index1, Index2


urlpatterns = [
    path('todo/', Index1.as_view(), name='index1'),
    path('todo/completed/', Index2.as_view(), name='index2'),
]