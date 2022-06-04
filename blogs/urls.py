from django.urls import path
from .views import make_blogs ,my_blogs , blogs,blogs_detail

urlpatterns = [
    path('', blogs, name='blogs' ),
    path('blogs_details/<slug:slug>/', blogs_detail , name='blog_one' ),
    path('make_blogs/', make_blogs , name='make_blogs' ),
    path('my_blogs/<str:user_u>/', my_blogs , name='my_blogs' ),

]