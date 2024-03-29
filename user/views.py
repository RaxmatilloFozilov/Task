from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        try:
            send_mail(
                subject='Welcome to',
                message='Welcome to',
                from_email='task@comsole.com',
                recipient_list=[request.POST['email'], 'task@comsole.com']
            )
            return HttpResponse('<h1>Welcome')
        except Exception as e:
            return HttpResponse(f'<h1>Somenthing went </h1> <p>{e}</p>', status=500)

    return render(request, 'bace.html')


def register_view(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserForm()
    return render(request, 'registration/register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {"form": form})



def logout_view(request):
    # Your logout logic here
    logout(request)
    return redirect('index')

def send_message(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email='task@comsole.com',
                recipient_list=[email]
            )
            return HttpResponse('<h1>Message sent successfully!</h1>')
        except Exception as e:
            return HttpResponse(f'<h1>Error occurred: {e}</h1>', status=500)

    return render(request, 'your_template.html')


def confirm_email(request):
    if request.method == 'POST':
        # Your email confirmation logic here
        pass
    else:
        # Your email confirmation form rendering logic here
        pass
    return render(request, 'registration/confirm_mail.html')


def register_or_login(request):
    return render(request, 'registration/login_or_register.html')