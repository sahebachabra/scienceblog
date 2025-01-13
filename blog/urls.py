from django.urls import path
from . import views  # Import the views module from the current directory
from django.contrib.auth import views as auth_views 
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Corrected to use 'views.'
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'), 
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', views.DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),  
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('register/', views.register, name='register'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('members/', include('members.urls')), 
]

    