from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('services/',services,name='services'),
    # path('blog/',blog,name='blog'),
    path('shop/',shop,name='shop'),
    path('galery/',galery,name='galery'),
    path('contact/',contact,name='contact'),

    # path('contact/',include('contact.urls')),
    path('blog/',include('blog.urls')),
]
