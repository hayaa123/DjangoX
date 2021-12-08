from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Blog


class BlogListView(ListView):
    template_name = "pages/blog_list.html"
    model = Blog


class BlogDetailView(DetailView):
    template_name = "pages/blog_detail.html"
    model = Blog


class BlogCreateView(CreateView):
    template_name = "pages/blog_create.html"
    model = Blog
    fields = ["title","image","description","user"]
    success_url = reverse_lazy("blog_list")

class BlogUpdateView(UpdateView):
    template_name = "pages/blog_update.html"
    model = Blog
    fields = ["title","image","description"]


class BlogDeleteView(DeleteView):
    template_name = "pages/blog_delete.html"
    model = Blog
    success_url = reverse_lazy("blog_list")