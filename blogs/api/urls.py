from django.urls import path
from .views import (
        PostAPIView,
        PostDetailAPIView,

        )


app_name = 'post_api'

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('posts/<slug:slug>/', PostDetailAPIView.as_view(), name='post'),

]