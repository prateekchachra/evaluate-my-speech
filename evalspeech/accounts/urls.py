from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts import views



urlpatterns=[


    #Login and logout forms
    re_path(r'^login/$', auth_views.LoginView.as_view(), {'template_name' : 'accounts/login.html'}),
    re_path(r'^logout/$', views.logout_view, {'next_page' : 'root:index'}, name='logout'),

    #Registration form
    re_path(r'^register/$', views.register_view, name='registration'),

    #Reset password form
    re_path(r'^reset-password/$', auth_views.PasswordResetView.as_view(), name='reset_password'),

    #Password reset done page
    re_path(r'^reset-password/done//$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    #Password reset confirm page
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    #Password reset complete page
    re_path(r'^reset-password/complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #To open your account
    re_path(r'^my_account/$', views.my_account_view, name='my_account'),

    #Editing user profile details
    re_path(r'^edit_details/$', views.edit_details_view, name='edit_details'),

    #Sending private emails to other members
    re_path(r'^private/$', views.private_post_view, name='private_post'),

    #Viewing profile of another user
    re_path(r'^profile/$', views.profile_view, name='profile_details'),
]