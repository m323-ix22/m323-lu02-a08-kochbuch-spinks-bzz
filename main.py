"""
A doc string
"""
import json

def adjust_recipe(recipe, persons_count: int):
    """
    A doc string
    """
    recipe["servings"] = persons_count
    return recipe

def load_recipe(recipes: str):
    """
    A doc string
    """
    return json.loads(recipes)

if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    RECIPE_JSON_A = '{"title": "Spaghetti Bolognese", "ingredients": '
    RECIPE_JSON_B = '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    recipe_json = f"{RECIPE_JSON_A}{RECIPE_JSON_B}"
    # Dein Code kommt hier hin
