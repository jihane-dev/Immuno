from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cours, Quiz, Question, Reponse, Resultat
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.db.models import Sum
from .models import Feedback
from .models import MediaImage, MediaAnimation, MediaVideo  # ajoute ces imports

def media_view(request):
    images = MediaImage.objects.all()
    animations = MediaAnimation.objects.all()
    videos = MediaVideo.objects.all()
    return render(request, 'quizz_app/media.html', {
        'images': images,
        'animations': animations,
        'videos': videos,
    })

# Vue pour la page d'accueil

def accueil(request):
    quiz_list = Quiz.objects.order_by('-date_creation')
    cours_list = Cours.objects.order_by('-date_publication')
    
 
    resultats = []
    if request.user.is_authenticated:
        resultats = Resultat.objects.filter(eleve=request.user).order_by('-date')[:1] 
        # Derniers scores
        
    classement = Resultat.objects.values('eleve__username') \
        .annotate(score_total=Sum('score')) \
        .order_by('-score_total')[:10]
        
    feedback_list = Feedback.objects.order_by('-date')[:10]


    return render(request, 'quizz_app/index.html', {
        'quiz_list': quiz_list,
        'cours_list': cours_list,
        'resultats': resultats,
        'classement': classement, # 🆕
        'feedback_list': feedback_list
        
    })

# Inscription
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Connexion automatique juste après inscription
            messages.success(request, f"Votre compte a bien été créé ! 🎉 Bienvenue sur Immuno-Fun, {user.username} !")
            return redirect('confirmation')  # 🔁 PAS de redirection immédiat
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def contact(request):
    return render(request, 'quizz_app/contact.html')


# Connexion
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')  # 👉 Redirection vers accueil après login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Déconnexion
def user_logout(request):
    logout(request)
    return redirect('login')

# Liste des cours
def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste_cours.html', {'cours': cours})

# Détail d’un cours
def detail_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    return render(request, 'cours/detail_cours.html', {'cours': cours})

# Liste des quiz
@login_required
def liste_quiz(request):
    quizs = Quiz.objects.all()
    return render(request, 'quiz/liste_quiz.html', {'quizs': quizs})

# Passer un quiz
@login_required
def passer_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        score = 0
        for question in questions:
            reponse_id = request.POST.get(f'question_{question.id}')
            if reponse_id:
                reponse = Reponse.objects.get(id=reponse_id)
                if reponse.est_correcte:
                    score += 1

        # Enregistrement du résultat
        Resultat.objects.create(eleve=request.user, quiz=quiz, score=score)
        return redirect('resultat_quiz', quiz_id=quiz.id)

    return render(request, 'quiz/passer_quiz.html', {'quiz': quiz, 'questions': questions})

# Résultat d’un quiz
@login_required
def resultat_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    resultat = Resultat.objects.filter(eleve=request.user, quiz=quiz).last()
    return render(request, 'quiz/resultat_quiz.html', {'quiz': quiz, 'resultat': resultat})


@login_required
def confirmation(request):
    return render(request, 'confirmation.html')


@login_required
def programme_view(request):
    return render(request, 'programme.html')

@login_required 
def l_cours(request):
    return render(request, 'l_cours.html')

@login_required
def t_cours(request):  # nom cohérent avec l'URL
    return render(request, 't_cours.html')  # nom exact du fichier

@login_required
@csrf_exempt
def envoyer_message_cours(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        email = request.POST.get('email', 'Non fourni')

        contenu = f"Nouvelle suggestion de cours :\n\n{message}\n\nAdresse e-mail : {email}"

        send_mail(
            subject="Suggestion de cours",
            message=contenu,
            from_email='ton_email@gmail.com',  # à configurer
            recipient_list=['jihane.jaiit@gmail.com'],  # à remplacer par ton adresse
        )

        return redirect('accueil')  # ou autre redirection
    
    
@login_required
def envoyer_feedback(request):
    if request.method == 'POST':
        note = int(request.POST.get('note', 0))
        commentaire = request.POST.get('commentaire')
        Feedback.objects.create(user=request.user, note=note, commentaire=commentaire)
        return redirect('accueil')
    
    
    