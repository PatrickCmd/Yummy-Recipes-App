"""class that creates user object"""

class User(object):
    """User object class"""

    def __init__(self, email, password, first_name = None,
                 last_name = None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.recipe_categories = []
        self.id = None
    
    def create_recipe_category(self, recipe_category):
        """User creates recipe category

            args:
                recipe_category->RecipeCategory object
        """
        # check if category already exists
        if [existing_category for existing_category in 
             self.recipe_categories if existing_category.name == \
               recipe_category.name]:
            return False
        self.recipe_categories.append(recipe_category)
        return True
    
    def get_recipe_categories(self):
        """Returns user recipe categories"""
        return self.recipe_categories
    
    def get_single_category(self, recipe_category_name):
        """Return single recipe category

            args:
                recipe_category_name->name ofobject of recipe \ 
                category to be returned
        """
        category = [category for category in self.recipe_categories 
                    if category.name == recipe_category_name]
        return category[0].description

    def edit_recipe_category(self, old_recipe_category_name, 
                              new_recipe_category_name, 
                              new_recipe_category_desc):
        """Updates recipe category object

            args:
                old_recipe_category_name-> name object of recipe category \
                to be updated
                new_recipe_category_name
        """
        pass