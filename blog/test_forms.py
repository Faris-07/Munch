class TestRecipeForm(TestCase):
    '''
    Testing for Recipe Form
    '''

    # Tests to check required fields are not blank

    def test_recipe_title_required(self):
        '''
        Test to ensure title is present
        '''
        form = RecipeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')