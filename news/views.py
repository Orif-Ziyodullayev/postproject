from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title','subtitle','date']

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

