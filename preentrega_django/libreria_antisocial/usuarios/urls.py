from django.urls import path
from .views import HomePageView, ArticleListView, ArticleDetailView, AboutView
from django.contrib.auth.views import LoginView, LogoutView
    
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]