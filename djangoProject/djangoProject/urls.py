from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from first_app import views
from first_app import urls


urlpatterns = [
    path('casdasda', views.index),
    path('trilha', views.index, include("first_app.urls")),
    path('admin/', admin.site.urls),
]
