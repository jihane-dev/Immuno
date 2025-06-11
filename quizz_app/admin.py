from django.contrib import admin
from .models import Cours, Quiz, Question, Reponse, Resultat
import json
from .models import Feedback
from .models import MediaImage, MediaAnimation, MediaVideo



class QuestionInline(admin.TabularInline):  # Ou admin.StackedInline pour un rendu plus vertical
    model = Question
    extra = 1  # Nombre de questions vides affichées pour ajouter rapidement

class QuizAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cours', 'date_creation')
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('texte', 'quiz', 'type_question')
    list_filter = ('type_question', 'quiz')
    search_fields = ('texte',)

    def donnees_pretty(self, obj):
        if obj.donnees:
            return json.dumps(obj.donnees, indent=2, ensure_ascii=False)
        return ""
    donnees_pretty.short_description = 'Données (JSON)'

    readonly_fields = ('donnees_pretty',)

    fieldsets = (
        (None, {
            'fields': ('quiz', 'texte', 'type_question')
        }),
        ('Données supplémentaires', {
            'fields': ('donnees', 'donnees_pretty'),
        }),
    )
    

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('note', 'commentaire', 'date')  # affichage en liste
    search_fields = ('commentaire',)               # champ de recherche
    list_filter = ('note',)                        # filtre par note 

admin.site.register(Cours)
admin.site.register(Quiz, QuizAdmin)  # Remarque : on utilise la classe QuizAdmin ici
admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse)
admin.site.register(Resultat)

admin.site.register(MediaImage)
admin.site.register(MediaAnimation)
admin.site.register(MediaVideo)