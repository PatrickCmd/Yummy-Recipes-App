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
        return category[0]

    def edit_recipe_category(self, old_recipe_category_name, 
                              new_recipe_category_name, 
                              new_recipe_category_desc):
        """Updates recipe category object

            args:
                old_recipe_category_name-> name object of recipe category \
                to be updated
                new_recipe_category_name-> name of new recipe category
                new_recipe_desc-> name of new recipe description
        """
        category = [category for category in self.recipe_categories 
                    if category.name == old_recipe_category_name]
        category[0].name = new_recipe_category_name
        category[0].description = new_recipe_category_desc
        return category

    def delete_recipe_category(self, recipe_category_name):
        """Deletes recipe category

            args:
                recipe_category_name->name of object to be deleted
        """
        category = [category for category in self.recipe_categories 
                    if category.name == recipe_category_name]
        category = category[0]
        self.recipe_categories.remove(category)
        return True
    
    def add_recipe(self, recipecategory, recipe):
        """Adds recipe to recipe category

            args:
                recipecategory->recipe category object
                recipe->object of recipe to be added to category
        """
        if [existing_recipe for existing_recipe in 
            recipecategory.recipes if existing_recipe.name ==  
             recipe.name]:
            return False
        recipecategory.recipes.append(recipe)
        return True 

    def get_recipes_from_category(self, recipecategory):
        """Get recipes in recipe category

            args:
                recipecategory->recipe category object
            Returns:
                A list of recipes in recipe category
        """
        return recipecategory.recipes

    def get_single_recipe_from_category(self, recipecategory, 
                                         recipe_name):
        """Get single recipe in recipe category

            args:
                recipecategory->recipe category object
                recipe_name->name of recipe in category
            Returns:
                A single recipe in recipe category
        """
        recipe = [existing_recipe for existing_recipe in 
                   recipecategory.recipes if existing_recipe.name ==  
                   recipe_name]
        return recipe[0]

    def edit_recipe_in_category(self, recipecategory, old_recipe_name, 
                                new_recipe_name, new_recipe_description):
        """Get single recipe in recipe category

            args:
                recipecategory->recipe category object
                recipe_name->name of recipe in category
            Returns:
                A single recipe in recipe category
        """
        recipe = [existing_recipe for existing_recipe in 
                   recipecategory.recipes if existing_recipe.name ==  
                   old_recipe_name]
        recipe[0].name = new_recipe_name
        recipe[0].description = new_recipe_description
        return True

    def delete_recipe_from_category(self, recipecategory, 
                                    recipe_name):
        """Get single recipe in recipe category

            args:
                recipecategory->recipe category object
                recipe_name->name of recipe in category
            Returns:
                A single recipe in recipe category
        """
        recipe = [existing_recipe for existing_recipe in 
                   recipecategory.recipes if existing_recipe.name ==  
                   recipe_name]
        recipecategory.recipes.remove(recipe[0])
        return True
