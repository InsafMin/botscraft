from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('create_bot/', create_bot, name='create_bot'),
    path('login/', login, name='login'),
    path('sign_up/', sign_up, name='sign_up'),
    path('contact/', contact, name='contact'),
    path('request/<int:request_id>/', show_request, name='request'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
