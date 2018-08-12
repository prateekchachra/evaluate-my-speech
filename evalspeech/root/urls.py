from django.urls import path
from root import views


urlpatterns=[
    path('', views.index, name='index')

]