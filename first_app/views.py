from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from first_app.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class HelloWorld(TemplateView):
  template_name = 'home.html'

class XiongBao(TemplateView):
  template_name = 'xiong.html'

class PostListView(ListView):
  model = Post
  template_name = 'post_master.html'

class PostDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class PostCreateView(CreateView):
  model = Post
  template_name = 'post_create.html'
  fields = '__all__'

class PostUpdateView(UpdateView):
  model = Post
  template_name = 'post_update.html'
  fields = ['title']

class PostDeleteView(DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('posts master')