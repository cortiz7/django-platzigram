"""Post views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
#from django.http import HttpResponse

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post 

# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    """View List posts."""
    template_name = "posts/feed.html"
    model = Post
    ordering = ("-created", )
    paginate_by = 5
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """View Detail post."""        
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """View Create a new post."""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context