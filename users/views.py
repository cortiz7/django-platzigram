#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views

#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

#Exception
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm, SignupForm


# Create your views

class UserDetailView(LoginRequiredMixin, DetailView):
    """User Detail view."""
    template_name = 'users/detail.html'
    queryset = User.objects.all()
    # es el atributo del url
    slug_field = 'username'
    slug_url_kwarg = 'username'    
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        """Add users posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    """User Signup View."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class ProfileUpdatView(LoginRequiredMixin, UpdateView):
    """Update Profile View."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    
    def get_object(self):
        """Return users profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})

class LoginView(auth_views.LoginView):
    """Login View."""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'
