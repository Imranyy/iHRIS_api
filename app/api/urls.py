from django.urls import path
from . import views

urlpatterns = [
    path('test',views.test, name='test'),
    path('',views.home, name='dashboard'),
    path('api/current_staff', views.all_current_staff, name='current_staff')
]