from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def home_view(request):
    return HttpResponse("Welcome to the FitAll application!")



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to the desired page after successful login
                return render(request, 'accounts/profile.html')  # Replace 'accounts/profile.html' with your profile page template
            else:
                # Invalid login, show an error message or handle it accordingly
                pass
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})




