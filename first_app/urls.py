from django.urls import path
from first_app import views


urlpatterns = [
  path('', views.HelloWorld.as_view(), name = 'hello world'),
  path('posts/', views.PostListView.as_view(), name = 'posts master'),
  path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post detail'),
  path('posts/new/', views.PostCreateView.as_view(), name = 'make post'),
  path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name = 'update post'),
  path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name = 'delete post'),
]