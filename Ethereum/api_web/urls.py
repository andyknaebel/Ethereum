from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views 


urlpatterns = [
 
    path('', views.api_webview),
    path('get_one', views.api_getone.as_view()),
    path('crypto', views.crypto.as_view()),
    path('Ethereum', views.crypto.as_view()),
]
