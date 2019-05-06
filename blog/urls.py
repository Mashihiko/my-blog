
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from blog.views import AboutMe_TemplateView, PostDetailView, PostListView, CategoryListView
#namespace = 'blog'

urlpatterns = [
    path('about_me/', AboutMe_TemplateView.as_view(), name='aboutme'),
    path('', PostListView.as_view(), name="post_list"),
    path('<category>/', CategoryListView.as_view(), name="post_category"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('programmming/', views.post_category_programming, name='post_category_programming'),
    path('cooking/', views.post_category_cooking, name='post_category_cooking'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

