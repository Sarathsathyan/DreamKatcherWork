from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI,dashboard
from django.urls import path

urlpatterns = [
    path('', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('dashboard/', dashboard.as_view() ,name='dash'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]