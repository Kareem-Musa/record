from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profiles:profile')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        action = 'دخول'
    return render(request, 'account/login.html', {'form': form, 'action': action})

# register view
def register(request):
    registered = False
    action = 'تسجيل'
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            # return redirect('profiles:profile')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form, 'action': action, 'registered': registered})


# logout view
@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('account:login'))
