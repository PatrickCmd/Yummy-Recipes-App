"""Class that creates recipe_category object"""

class RecipeCategory(object):
    """ Recipe category object classs"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.recipes = []
        