class TestRecipeForm(TestCase):
    '''
    Testing for Recipe Form
    '''

    # Tests to check required fields

    def test_recipe_title_required(self):
        '''
        Test to ensure title is required
        '''
        form = RecipeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_recipe_description_required(self):
        '''
        Test to ensure description is required
        '''
        form = RecipeForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.'
            )

    def test_recipe_ingredients_required(self):
        '''
        Test to ensure ingredients is required
        '''
        form = RecipeForm({'ingredients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(
            form.errors['ingredients'][0], 'This field is required.'
            )

    def test_recipe_method_required(self):
        '''
        Test to ensure method is required
        '''
        form = RecipeForm({'method': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(form.errors['method'][0], 'This field is required.')
