from django.urls import path, re_path
from egor.views import *
from egor import views

urlpatterns = [
    path('fullname/', views.fullname, kwargs={'name': 'egor', 'username': 'teptev'}),
    path('fullname/age/', views.age, name='age', kwargs={'age_': '18'}),
    path('fullname/age/interesting/', views.interesting, kwargs={'int_': 'hr'}),
    path('fullname/age/interesting/about/', about, kwargs={'number': 'i dont like to do homework'}),
    path('fullname/age/interesting/about/contact', contact, kwargs={'contacts': 'https://github.com/, 935892358, telegram'})
]
