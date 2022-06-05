from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class HomeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('-published_on')
    template_name = 'index.html'
    paginate_by = 6
