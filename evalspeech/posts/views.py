from django.shortcuts import render
from django.http import HttpResponse


def posts(request):
    return render(request, 'post.html')

def latest_posts(request):
    return render(request, 'latest.html')