from django.urls import path, re_path
from root import views


urlpatterns=[
    path('', views.index, name='index'),
    re_path(r'^evaluations-guide/$', views.eval_guide, name='eval_guide'),
    re_path(r'^public-posts/$', views.public_posts, name='public_posts'),
]