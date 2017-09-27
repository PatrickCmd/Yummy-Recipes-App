"""Class that creates recipe_category object"""

class RecipeCategory(object):
    """ Recipe category object classs"""

    def __init__(self, name, description, user_id=None):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.recipes = []
        