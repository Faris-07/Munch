import unittest
from django.contrib.auth.models import User
from .models import Recipe, Comment

class TestViews(unittest.TestCase):
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