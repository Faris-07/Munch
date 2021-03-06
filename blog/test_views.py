from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment
"""
Importing TestCase for unit testing and Recipe and Comment models from blog.models
"""


class TestViews(TestCase):
    """
    Testing for Views
    """
    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        self.recipe = Recipe.objects.create(title='Test', author=test_user)
        self.comment = Comment.objects.create(
            body='Test Comment', recipe=self.recipe
            )
        self.client.login(username='testuser', password='testpw')

    # Tests to display pages

    def test_get_home_page(self):
        """
        Test to ensure home page is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_all_recipes_page(self):
        """
        Test to ensure recipes page is displayed
        """
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    def test_get_recipe_detail_page(self):
        """
        Test to ensure recipe details page is displayed
        """
        response = self.client.get(f'/{self.recipe.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_get_searched_recipe_page(self):
        """
        Test to ensure searched results page is displayed
        """
        response = self.client.get('/search_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_recipe.html')

    def test_get_add_recipes_page(self):
        """
        Test to ensure add recipes page is displayed
        """
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_get_liked_recipes_page(self):
        """
        Test to ensure liked recipes page is displayed
        """
        response = self.client.get('/liked_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'liked_recipes.html')

    def test_get_edit_recipe_page(self):
        """
        Test to ensure edit recipe page is displayed
        """
        response = self.client.get(f'/edit_recipe/{self.recipe.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')

    # Tests for page functionality

    def test_add_recipe(self):
        """
        Testing recipes can be added to database
        """
        self.client.post('/add_recipe/', {
            'title': 'Test',
            'description': 'Test',
            'ingredients': 'Test',
            'method': 'Test'
        })
        new_recipe = Recipe.objects.filter(title='Test')
        self.assertEqual(len(new_recipe), 1)

    def test_edit_recipe(self):
        """
        Test editing a recipe
        """
        self.client.post(f'/edit_recipe/{self.recipe.id}', {
            'title': 'Test',
            'description': 'Edited Description',
            'ingredients': 'Test',
            'method': 'Test'
        })
        edited_recipe = Recipe.objects.first().description
        self.assertEqual(edited_recipe, "Edited Description")

    def test_add_comment(self):
        """
        Testing comments can be added to database
        """
        self.client.post(f'/{self.recipe.slug}/', {'body': 'Test comment with fries'})
        self.assertEqual(Comment.objects.last().body, "Test comment with fries")

    def test_like_button(self):
        """
        Testing like button when recipe is liked
        """
        response = self.client.post(f'/like/{self.recipe.slug}')
        self.assertRedirects(response, f'/{self.recipe.slug}/')
        is_user_present = self.recipe.likes.filter(id=1).exists()
        self.assertTrue(is_user_present)
        response = self.client.post(f'/like/{self.recipe.slug}')
        is_user_present = self.recipe.likes.filter(id=1).exists()
        self.assertFalse(is_user_present)

    def test_search_bar_returns_searched_word_results(self):
        """
        Testing the search bar results for the word/recipe searched is returned
        """
        searched = 'Test'
        recipes = Recipe.objects.filter(title__icontains=searched)
        response = self.client.post('/search_recipe/', {
            'searched': searched,
            'recipes': recipes
        })
        self.assertEqual(response.context['searched'], 'Test')
        self.assertEqual(len(response.context['recipe']), 1)
