import datetime

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail,BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from datetime import datetime
from deep_translator import GoogleTranslator
from blogs.services import get_blogs_all

from .forms import UserForm

def index(request):
    lan_code = 'en'
    key_word = request.GET.get("search")
    time = datetime.now().strftime("%H:%M:%S")
    user1 = request.user.get_username()
    searching_word = GoogleTranslator(source='auto', target='en').translate(f'{key_word}')
    forms = get_blogs_all(key_word,searching_word)
    print("N"*23,searching_word)
    ctx = {
        "user1":user1,
        'time':time,
        "forms": forms,
        "uz": "uz",
        "ru": "ru",
        "eng": "en",
        "lan_code": lan_code
    }
    return render(request, 'home.html',ctx)

def index2(request,coder):
    lan_code = coder
    key_word = request.GET.get("search")
    time = datetime.now().strftime("%H:%M:%S")
    user1 = request.user.get_username()
    searching_word = GoogleTranslator(source='auto', target='en').translate(f'{key_word}')
    forms = get_blogs_all(key_word,searching_word)
    print("N"*23,searching_word)
    ctx = {
        "user1":user1,
        'time':time,
        "forms": forms,
        "uz": "uz",
        "ru": "ru",
        "eng": "en",
        "lan_code": lan_code
    }
    return render(request, 'home.html',ctx)

def registration(request):

   if request.POST:
       form = UserForm(request.POST)



       if form.is_valid():

           form.save()
           messages.success(request, 'SUCCESSFULLY REGISTERED !!!')
           return redirect('login')

       else:
           messages.error(request, 'OOPS ! SOMETHING WRONG! TRY AGAIN!')




   forms = UserForm()
   ctx = {
        "forms": forms
    }

   return render(request, 'register/register.html', ctx)

def login_user(request):



    if request.POST:
        form = AuthenticationForm(request , data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'SOMETHING WRONG!')

        else:
            messages.error(request, 'SOMETHING WRONG !!')

    forms = AuthenticationForm()
    ctx = {
        'forms': forms
    }

    return render(request, 'register/login.html', ctx)

def logout_user(request):
    logout(request)
    return redirect('home')

def password_set(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "register/password_reset.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'NexusPlus - Classified Ads and Listing Template',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'mirzoyevogabek1@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done")
    password_reset_form = PasswordResetForm()
    return render(request,'register/forgot-password.html',  {
        "password_reset_form":password_reset_form
    })
# Create your views here.

