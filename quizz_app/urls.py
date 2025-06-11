from django.urls import path
from . import views
from django.urls import path



urlpatterns = [
    path('media/', views.media_view, name='media'),
    path('', views.accueil, name='accueil'),  # Page d'accueil
    path('contact/', views.contact, name='contact'),
    # Authentification
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('programme/', views.programme_view, name='programme'),
  

    # Cours
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/<int:cours_id>/', views.detail_cours, name='detail_cours'),

    # Quiz
    path('quiz/', views.liste_quiz, name='liste_quiz'),
    path('quiz/<int:quiz_id>/', views.passer_quiz, name='passer_quiz'),
    path('quiz/<int:quiz_id>/resultat/', views.resultat_quiz, name='resultat_quiz'),
    
    # Cours
    path('liste-cours/', views.l_cours, name='l_cours'),
    path('t_cours/', views.t_cours, name='t_cours'),  # à créer aussi
    
    path('envoyer-message-cours/', views.envoyer_message_cours, name='envoyer_message_cours'),

    path('feedback/', views.envoyer_feedback, name='envoyer_feedback'),

]
