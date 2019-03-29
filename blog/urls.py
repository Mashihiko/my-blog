from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
#namespace = 'blog' 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/プログラミング/', views.post_category_programming, name='post_category_programming'),
    path('post/料理/', views.post_category_cooking, name='post_category_cooking'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    #path( '', TemplateView.as_view(template_name='blog/post_list.html'), name='post_list'),
    #path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

