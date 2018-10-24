from django.urls import path
from . import views
from .views import Post_list, Post_detail, Post_new

urlpatterns = [
    path('', Post_list.as_view(), name='post_list'),
    path('post/<int:pk>/', Post_detail.as_view(), name='post_detail'),
    path('post/new/', Post_new.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]