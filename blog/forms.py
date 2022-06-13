from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
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
