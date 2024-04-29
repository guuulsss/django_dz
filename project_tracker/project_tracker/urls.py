from django.contrib import admin
from django.urls import path, include
from tasks.views import index

urlpatterns = [
    path('', index),
    path('tasks/', include('tasks.urls')),
    path('quality_control/', include('quality_control.urls')),
    path('admin/', admin.site.urls),
]
