from django.urls import path
from django.contrib.auth import views as auth_views
from home import views
# from .views import Home

urlpatterns = [
    
    path('', views.index, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('register/', views.register, name="register"),
    path('transcribe/', views.transcribe, name="transcribe"),


]