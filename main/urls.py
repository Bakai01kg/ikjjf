from django.urls import path
from .views import ProfileDetailView, UserRegisterView,ProfileList

urlpatterns = [
      path('register/',UserRegisterView.as_view(),name = 'register'),
      path('profile/',ProfileList.as_view(),name='profile'),
      path('profile/<int:pk>/',ProfileDetailView.as_view())
 ]




