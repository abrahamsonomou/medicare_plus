from django.contrib import admin
from .models import *

# Register your models here.
# Blog
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','auteur','categorie','created')
    list_filter=('titre','auteur',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(ArticleCategorie)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)
    list_filter=('nom_categorie',)
    prepopulated_fields={'slug':('nom_categorie',)}


# admin.site.register(Tag)
