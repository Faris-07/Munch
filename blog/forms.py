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
            "serves",
            "cook_time",
            "method",
            "image",
            "image_url",
        )
        widgets = {
            "description": SummernoteWidget(),
            "ingredients": SummernoteWidget(),
            "serves": SummernoteWidget(),
            "cook_time": SummernoteWidget(),
            "method": SummernoteWidget(),
        }

