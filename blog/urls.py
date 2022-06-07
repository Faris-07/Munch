from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail")
] 
