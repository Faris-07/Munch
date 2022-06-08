from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm

# Create your views here.

class HomeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('-published_on')
    template_name = 'index.html'

class RecipeView(generic.ListView):
    model = Recipe
    template_name = "recipes.html"
    paginate_by = 6 

class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        ) 