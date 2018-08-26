from django.urls import path, re_path
from posts import views


urlpatterns=[
    re_path(r'id/^(?P<post_id>[a-zA-Z0-9]+)$', views.posts, name='posts'),
    re_path(r'^latest$', views.latest_posts, name='latest_posts'),

]