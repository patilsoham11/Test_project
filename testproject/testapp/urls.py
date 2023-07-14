from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('home/', views.index, name='index'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    
]