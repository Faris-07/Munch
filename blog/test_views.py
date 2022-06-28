from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


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