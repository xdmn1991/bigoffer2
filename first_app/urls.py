from django.urls import path
from first_app import views


urlpatterns = [
  path('', views.HelloWorld.as_view(), name = 'hello_word'),
  path('posts/', views.PostListView.as_view(), name = 'posts_master'),
  path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
]