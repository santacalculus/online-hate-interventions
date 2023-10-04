from django.urls import path
from blog import views

urlpatterns = [
    path('', views.base_action, name='page'),
    path('login', views.login_action, name='login'),
    path('value', views.value_action, name='value'),
    path('page/<int:id>', views.base_action, name='page'),
    path('register', views.register_action, name='register'),
    path('page2/<int:id>', views.display_action, name='page2'),
    path('logout', views.logout_action, name='logout'),
]