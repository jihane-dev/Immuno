from django.db import models
from django.contrib.auth.models import User

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)  # ✅ Ajouté

    def __str__(self):
        return self.titre

class Quiz(models.Model):
    titre = models.CharField(max_length=100)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)  # Ajoute ceci

    def __str__(self):
        return self.titre

class Question(models.Model):
    TYPE_CHOICES = [
        ('qcm', 'QCM'),
        ('vrai_faux', 'Vrai/Faux'),
        ('drop', 'Drop'),
        ('puzzle', 'Puzzle'),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    texte = models.CharField(max_length=300)
    type_question = models.CharField(max_length=20, choices=TYPE_CHOICES, default='qcm')
    donnees = models.JSONField(blank=True, null=True)  # ✅ Ajouté pour le champ utilisé dans admin.py

    def __str__(self):
        return self.texte

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    texte = models.CharField(max_length=200)
    est_correcte = models.BooleanField(default=False)

    def __str__(self):
        return self.texte

class Resultat(models.Model):
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.eleve.username} - {self.quiz.titre} : {self.score}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField()
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.note} ⭐)"
    
    from django.db import models

class MediaImage(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # va sur Cloudinary

    def __str__(self):
        return self.nom

class MediaAnimation(models.Model):
    nom = models.CharField(max_length=100)
    animation = models.FileField(upload_to='animations/')  # .mp4, .gif...

    def __str__(self):
        return self.nom

class MediaVideo(models.Model):
    titre = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')  # .mp4

    def __str__(self):
        return self.titre
