"""Platzigram middleware catalog  """

#Django 
from django.shortcuts import redirect
from django.urls import reverse

#Models
from users.models import Profile

class ProfileCompletionMiddleware:
    """Profile completion middleware  
    
    Ensure every user that is interacting with thw platform
    have their profile picture and biography
    """

    def __init__(self, get_response):
        """ Middleware inizialition """
        self.get_response = get_response
    
    def __call__(self, request):
        """ Code to be executed for each request before the view is called """
        if not request.user.is_anonymous:
            #profile = request.user.profile
            if not request.user.is_staff:
                profile = Profile(user=request.user)
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response 
            

