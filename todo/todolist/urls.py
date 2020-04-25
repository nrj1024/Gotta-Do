from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login',views.loginuser, name='login'),
    path('logout',views.logoutuser, name='logout'),
    path('task_view/<list_id>', views.task_view, name='task_view')
]