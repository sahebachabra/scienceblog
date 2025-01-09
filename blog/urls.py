from django.urls import path
from . import views  # Import the views module from the current directory
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Corrected to use 'views.'
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'), 
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', views.DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),  # Corrected to use 'views.'
    path('register/', views.register, name='register'),  # Add this line for the register view
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
