from django.shortcuts import render
from django.contrib.messages import get_messages
from .models import SpeechPost

latest_posts = SpeechPost.objects.order_by('-pub_date')[:3]

def index(request):
    storage = get_messages(request)
    logged_out_user = None
    for message in storage:
        logged_out_user = message
        break


    context = {
        'latest_posts' : latest_posts[:3],
        'logged_out_user' : logged_out_user
    }
    return render(request, 'home/index.html', context)


def eval_guide(request):
    return render(request, 'home/eval_guide.html')

def public_posts(request):
    context = {
        'latest_posts' : latest_posts,
    }
    return render(request, 'home/public_posts.html', context)
