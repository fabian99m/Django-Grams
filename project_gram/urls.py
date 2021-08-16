
from django.contrib import admin
from django.urls import path

from project_gram import views as local_views
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', local_views.hola),
    path('fecha/', local_views.fecha),
    path('sayhi/<str:name>/<int:age>', local_views.sayhi),
    path('posts/', post_views.list_posts)
]
