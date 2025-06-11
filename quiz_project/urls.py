from django.contrib import admin
from django.urls import path, include
from quizz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/<int:cours_id>/', views.detail_cours, name='detail_cours'),
    path('quiz/', views.liste_quiz, name='liste_quiz'),
    path('quiz/<int:quiz_id>/', views.passer_quiz, name='passer_quiz'),
    path('quiz/<int:quiz_id>/resultat/', views.resultat_quiz, name='resultat_quiz'),
    path('', include('quizz_app.urls')),  # Utilise l'URL d'accueil de quizz_app
]
