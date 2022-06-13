from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('edit_recipe/<int:pk>', views.EditRecipe.as_view(), name='edit_recipe'),
    path('delete_recipe/<str:pk>', views.DeleteRecipe, name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name="recipe_like"),
    path('search', views.SearchRecipe, name='search_recipe'),
]
