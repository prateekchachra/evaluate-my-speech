from django.urls import path, re_path
from accounts import views


urlpatterns=[
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^my_account/$', views.my_account_view, name='my_account'),
    re_path(r'^edit_details/$', views.edit_details_view, name='edit_details'),
    re_path(r'^private/$', views.private_post_view, name='private_post'),
    re_path(r'^profile/$', views.profile_view, name='profile_details'),
]