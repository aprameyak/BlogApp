from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
