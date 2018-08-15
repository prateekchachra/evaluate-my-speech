from django.shortcuts import render
from django.http import HttpResponse

import random


def login_view(request):
    return render(request, 'registration/login_view.html')


def logout_view(request):
    return render(request, 'registration/logout_view.html')


def my_account_view(request):
    return render(request, 'account_settings/my_account.html')

def profile_view(request):
    return render(request, 'profile/profile.html')

def private_post_view(request):
    return render(request, 'profile/create_private_post.html')

def edit_details_view(request):
    return render(request, 'account_settings/edit_details.html')


