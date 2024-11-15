from django.shortcuts import render,get_object_or_404

from .models import Profile


# Create your views here.

def profile_view(request, username):
    user = get_object_or_404(Profile, username=username)
    return render(request, 'profiles/profile.html', {'user': user})
