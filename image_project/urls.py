from django.contrib import admin
from django.urls import path
from images import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('fetchdata/<str:query>/', views.fetch_images_api, name='fetch_images_api'),
    path('show-images/', views.show_images, name='show_images'),
    path('register/',views.register_user,name='register_user'),
    path('login/',views.login_user,name='login_user'),
]