from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import RegistrationForm, EditProfileForm

def login_view(request):

    return render(request, 'registration/login.html')


def logout_redirect(request):
    logged_in_user = ''
    if(request.user) :
        messages.add_message(request, messages.INFO, request.user.username)
    auth_logout(request)
    return redirect('/')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('account_settings/my_account')
    else:
        form = RegistrationForm()

        context = {'form' : form}
        return render(request, 'registration/register_form.html', context)



@login_required
def my_account_view(request):
    context = {
        'user' : request.user,
    }
    return render(request, 'account_settings/my_account.html', context)

def profile_view(request):
    return render(request, 'profile/profile.html')

def private_post_view(request):
    return render(request, 'profile/create_private_post.html')

def edit_details_view(request):
    if(request.method=='POST'):
        form = EditProfileForm(request.POST, instance=request.user)

        if(form.is_valid()):
            form.save()
            context = {
                #If true, we will tell the user that the edit was successful and display the updated information
                'change_flag' : True
            }
            return redirect('account_settings/my_account', context)

    else:
        form = EditProfileForm(instance=request.user)
        context = {
        'form' : form,
        }
        return render(request, 'account_settings/edit_details.html', context)


def people_near_me_view(request):
    return render(request, 'people/near_me.html')