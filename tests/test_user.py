import unittest

from classes.user import User
from classes.recipe_category import RecipeCategory


class TestUsercase(unittest.TestCase):

    def setUp(self):
        self.user = User('pwalukagga@gmail.com', 'pato123')
        self.recipe_category = RecipeCategory('Luwombo', 'Delicious Luwombo')
    
    def test_create_recipe_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.assertEqual(len(self.user.recipe_categories), 1)
        self.recipe_category = RecipeCategory('Vegetables', 
                                                'Vegetable recipe')
        self.user.create_recipe_category(self.recipe_category)
        self.recipe_category = RecipeCategory('Breakfast sandwich', 
                                                'Sandwich recipe for breakfast')
        self.user.create_recipe_category(self.recipe_category)
        self.assertEqual(len(self.user.recipe_categories), 3)
        index = len(self.user.recipe_categories) - 1
        self.assertEqual(self.user.recipe_categories[index].name, 
                          'Breakfast sandwich')
        self.assertEqual(self.user.recipe_categories[index].description, 
                          'Sandwich recipe for breakfast')
    
    def test_create_recipe_category_category_already_exists(self):
        self.user.create_recipe_category(self.recipe_category)
        self.recipe_category = RecipeCategory('Luwombo', 'Delicious Luwombo')
        self.assertFalse(self.user.create_recipe_category(self.recipe_category))

if __name__ == '__main__':
    unittest.main()
