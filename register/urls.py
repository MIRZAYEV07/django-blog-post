from django.urls import path
from .views import index, registration, login_user, logout_user , password_set ,index2

urlpatterns = [
    path('', index, name = 'home'),
    path('<str:coder>/', index2 , name='home2'),
    path('register/', registration, name = 'registration'),
    path('login/', login_user, name = 'login'),
    path('logout', logout_user, name = 'logout'),
    path('forgotpassword' , password_set ,name = 'forgot_password')
]