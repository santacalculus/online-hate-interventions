from django.urls import path
from blog import views

urlpatterns = [
    path('', views.base_action, name='page'),
    path('login', views.login_action, name='login'),
    path('page/<int:id>', views.base_action, name='page'),
    path('register', views.register_action, name='register'),
    path('logout', views.logout_action, name='logout'),
]