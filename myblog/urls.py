from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('',views.welcome,name='holi'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]