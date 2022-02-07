from django.urls import path
from . import views

urlpatterns = [
    path('cache/clear',views.clear_cache, name='cache-clear'),
    path('current_staff', views.all_current_staff, name='current_staff'),
    path('user_accounts',views.user_account, name='user_account')
]