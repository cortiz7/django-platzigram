"""Form Post."""

# Django
from django import forms

#Models
from posts.models import Post


#Forms
class PostForm(forms.ModelForm):
    """Post ModelForm."""

    class Meta:
        """Form settings."""
        model = Post
        fields = ('user', 'title', 'photo')

