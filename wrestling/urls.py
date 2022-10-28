from django.contrib import admin
from django.urls import path,include
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('api-auth/',include('rest_framework.urls')),
    path('auth/',include('djoser.urls'))
]
