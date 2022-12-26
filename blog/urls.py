from django.urls import path
from blog import views

urlpatterns = [
    path('', views.base_action, name='page'),
]