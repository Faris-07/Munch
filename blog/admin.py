from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Recipe)
class AdminRecipe(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'published_on')
    prepopulated_fields = {'slug': ('author', 'title')}
    summernote_fields = ('ingredients', 'method')
