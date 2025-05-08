from django.contrib import admin
from django.urls import path, include  # Inclure 'include' pour les URLs de l'application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # Inclure les URLs définies dans l'app 'courses'
]

