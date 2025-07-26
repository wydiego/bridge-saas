from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
