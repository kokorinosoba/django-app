from django.urls import path
from . import views


urlpatterns = [
    path('checkbox', views.demo3, name='demo3'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.calc_credit, name='calc_credit')
]
