from django.contrib.auth import authenticate, login as auth_login,logout

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['u_name']
            email = form.cleaned_data['u_email']
            password = form.cleaned_data['u_pass']

            # Create a new user
            user = User.objects.create_user(username, email, password)
            return redirect('login')

        else:
            # Show an error message
            messages.error(request, 'Invalid form data. Please try again.')

    form = RegisterForm()
    dict_form = {'form': form}
    return render(request, 'registration.html', dict_form)


def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['pass_word']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            auth_login(request, user)
            # Redirect to the home page or some other page
            return redirect('/')
        else:
            # Show an error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')