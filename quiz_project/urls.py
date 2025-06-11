from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizz_app.urls')),  # Toutes les URLs de quizz_app sont ici
]
