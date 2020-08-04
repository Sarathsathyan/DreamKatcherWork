from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.register,name="reg"),
    path('login/',views.login,name="logi")


]
