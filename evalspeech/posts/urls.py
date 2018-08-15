from django.urls import path, re_path
from posts import views


urlpatterns=[
    re_path(r'^posts/(?P<post_id>[a-zA-Z0-9]+)$', views.posts, name='posts'),
]