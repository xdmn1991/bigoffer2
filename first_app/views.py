from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from first_app.models import Post

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