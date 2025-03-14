from django.urls import path
from .import views
urlpatterns=[
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('booking/', views.booking, name='booking'),
    path('event/', views.event, name='event'),
    path('food/', views.food, name='food'),
    path('gall/', views.gall, name='gall'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('key/', views.key, name='key'),
    path('ar/', views.ar, name='ar'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
