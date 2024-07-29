from django.urls import path
from .views import GoogleLoginView, GoogleLogoutView

urlpatterns = [
    path('login/', GoogleLoginView.as_view(), name='google_login'),
    path('logout/', GoogleLogoutView.as_view(), name='google_logout'),
]
