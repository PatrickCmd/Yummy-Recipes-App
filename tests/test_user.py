import unittest

from classes.user import User
from classes.recipe_category import RecipeCategory
from classes.recipe import Recipe


class TestUsercase(unittest.TestCase):

    def setUp(self):
        self.user = User('pwalukagga@gmail.com', 'pato123')
        self.recipe_category = RecipeCategory('Luwombo', 'Delicious Luwombo')
        self.recipe = Recipe('Meat Luwombo', 'Spectacular local source food')
    
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
    
    def test_get_recipe_caategories(self):
        self.user.create_recipe_category(self.recipe_category)
        self.recipe_category = RecipeCategory('Chicken Vegetables', 
                                               'Delicious Luwombo')
        self.user.create_recipe_category(self.recipe_category)
        self.assertEqual(len(self.user.get_recipe_categories()), 2)

    def test_get_single_recipe_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.recipe_category = RecipeCategory('Chicken Vegetables', 
                                               'Delicious Luwombo')
        self.assertEqual(self.user.get_single_category('Luwombo').description, 
                                             'Delicious Luwombo')
    
    def test_edit_recipe_category(self):
        self.recipe_category = RecipeCategory('Chicken Vegetables', 
                                               'Delicious Luwombo')
        self.user.create_recipe_category(self.recipe_category)
        self.user.edit_recipe_category('Chicken Vegetables',
                                        'Chicken Sandwich', 
                                        'Sweet Sandwich')
        self.assertEqual(self.recipe_category.name, 'Chicken Sandwich')
        self.assertEqual(self.recipe_category.description, 
                         'Sweet Sandwich')
    
    def test_delete_recipe_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.recipe_category = RecipeCategory('Chicken Vegetables', 
                                               'Delicious Luwombo')
        self.user.create_recipe_category(self.recipe_category)
        self.recipe_category = RecipeCategory('Omlet Vegetables', 
                                               'Delicious Omlet')
        self.user.create_recipe_category(self.recipe_category)
        self.assertEqual(len(self.user.recipe_categories), 3)
        self.user.delete_recipe_category('Chicken Vegetables')
        self.assertEqual(len(self.user.recipe_categories), 2)
    
    def test_add_recipes(self):
        """Adds recipes to recipe category
        """
        self.user.create_recipe_category(self.recipe_category)
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 1)
        self.recipe = Recipe('Chicken Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.recipe = Recipe('Vegetable Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 3)
    
    def test_get_recipes_from_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 1)
        self.recipe = Recipe('Chicken Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.recipe = Recipe('Vegetable Luwombo', 
                             'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(
            len(self.user.get_recipes_from_category(self.recipe_category)), 
            3)
    
    def test_get_single_recipe_from_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 1)
        self.recipe = Recipe('Chicken Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(self.user.get_single_recipe_from_category(
                          self.recipe_category, 'Chicken Luwombo'
                          ).name, 
                          'Chicken Luwombo')
        self.assertEqual(self.user.get_single_recipe_from_category(
                          self.recipe_category, 'Chicken Luwombo'
                          ).description, 
                          'Spectacular local source food')

    def test_edit_recipe_in_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 1)
        self.recipe = Recipe('Chicken Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.user.edit_recipe_in_category(self.recipe_category,
                                           'Chicken Luwombo',
                                           'Chicken Recipe Luwombo', 
                              'Spectacular Recipe local source food')
        self.assertEqual(self.recipe_category.recipes[1].name, 
                          'Chicken Recipe Luwombo')
                
    
    def test_delete_recipe_from_category(self):
        self.user.create_recipe_category(self.recipe_category)
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 1)
        self.recipe = Recipe('Chicken Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.recipe = Recipe('Vegetable Luwombo', 
                              'Spectacular local source food')
        self.user.add_recipe(self.recipe_category, self.recipe)
        self.assertEqual(len(self.recipe_category.recipes), 3)
        self.user.delete_recipe_from_category(self.recipe_category, 
                                              'Vegetable Luwombo')
        self.assertEqual(len(self.recipe_category.recipes), 2)


if __name__ == '__main__':
    unittest.main()
