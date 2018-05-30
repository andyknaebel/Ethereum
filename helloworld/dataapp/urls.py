
from django.urls import include, path
from django.conf.urls import url
from .import views 


urlpatterns = [
    url(r'^blog/blog/(?P<id>\d+)/$', views.blog, name='blog'), 
    url(r'^add/blog/$', views.add_blog, name='add_blog'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    path('', views.dataview),
]

