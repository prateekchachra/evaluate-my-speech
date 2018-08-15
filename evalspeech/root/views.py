from django.shortcuts import render

from .models import SpeechPost

latest_posts = SpeechPost.objects.order_by('-pub_date')[:3]

def index(request):
    context = {
        'latest_posts' : latest_posts[:3],
    }
    return render(request, 'home/index.html', context)


def eval_guide(request):
    return render(request, 'home/eval_guide.html')

def public_posts(request):
    context = {
        'latest_posts' : latest_posts,
    }
    return render(request, 'home/public_posts.html', context)
