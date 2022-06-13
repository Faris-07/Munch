from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.views.generic import CreateView
from .models import Recipe
from .forms import CommentForm, RecipeForm

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

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class RecipeLike(View):
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class AddRecipe(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'


def SearchRecipe(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        recipes = Recipe.objects.filter(title__icontains=searched)
        return render(
            request, "search_recipe.html", {"searched": searched, "recipes": recipes}
        )
    else:
        return render(request, "search_recipe.html")
