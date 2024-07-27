from django.contrib import admin
from django.urls import path
from images import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.login_view, name='login'),
    path('fetchdata/<str:query>/', views.fetch_images, name='fetch_images'),
    path('show-images/', views.show_images, name='show_images'),
]