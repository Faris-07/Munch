from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name="recipe_like"),
    path('search', views.SearchRecipe, name='search_recipe'),
] 
