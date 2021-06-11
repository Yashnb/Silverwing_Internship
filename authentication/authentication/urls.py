from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('Home.urls')),
    path('accounts/', include('allauth.urls')),
]
