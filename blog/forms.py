from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """Comments form"""
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """Recipe Form"""
    class Meta:
        model = Recipe
        fields = (
            "title",
            "description",
            "ingredients",
            "method",
            "serves",
            "cook_time",
            "image",
            "image_url",
        )
        widgets = {
            "description": SummernoteWidget(),
            "ingredients": SummernoteWidget(),
            "method": SummernoteWidget(),
        }
