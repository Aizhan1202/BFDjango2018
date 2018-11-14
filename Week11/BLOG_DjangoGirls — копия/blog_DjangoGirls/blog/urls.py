from django.urls import path
from . import views
#from .views import Post_list, Post_detail, Post_new, Post_publish, Post_remove, ListMyPosts
from .views import PostList, PostDetail, CreatePost
urlpatterns = [
#    path('', Post_list.as_view(), name='post_list'),
 #   path('post/<int:pk>/', Post_detail.as_view(), name='post_detail'),
  #  path('post/new/', Post_new.as_view(), name='post_new'),
   # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
   # path('post/<int:pk>/publish/', Post_publish.as_view(), name='post_publish'),
   # path('post/<int:pk>/remove/', Post_remove.as_view(), name='post_remove'),
   # path('my_posts/', ListMyPosts.as_view(), name='my_posts'),
   # path('login/', views.login, name='login'),
   # path('register/', views.register, name='register'),
   # path('logout/', views.logout, name='logout'),
   # path('post_rest/', views.post_list),
   # path('post_rest/<int:pk>/', views.post_detail),
    path('post_gbv/', PostList.as_view()),
    path('post_gbv/<int:pk>/', PostDetail.as_view()),
    path('post_gbv/create', CreatePost.as_view())
]