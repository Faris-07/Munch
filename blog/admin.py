from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Recipe)
class AdminRecipe(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'published_on')
    search_fields = ['title', 'description', 'ingredients']
    prepopulated_fields = {'slug': ('author', 'title')}
    list_filter = ('published_on', 'author')
    summernote_fields = ('ingredients', 'method')

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):

    search_fields = ('name', 'email', 'body')
    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('created_on', )
