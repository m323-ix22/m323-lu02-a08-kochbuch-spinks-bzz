"""
A doc string
"""
import json

def adjust_recipe(recipe, persons_count: int):
    """
    A doc string
    """
    n = recipe["servings"] / persons_count
    for i in recipe["ingredients"]:
        recipe["ingredients"][i] = recipe["ingredients"][i] / n
    recipe["servings"] = persons_count
    return recipe

def load_recipe(recipes: str):
    """
    A doc string
    """
    return json.loads(recipes)

if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    RECIPE_JSON_A = "{\"title\": \"Spaghetti Bolognese\", \"ingredients\": "
    RECIPE_JSON_B = "{\"Spaghetti\": 400, \"Tomato Sauce\": 300, "
    RECIPE_JSON_C = "\"Minced Meat\": 500}, \"servings\": 4}"
    recipe_json = f"{RECIPE_JSON_A}{RECIPE_JSON_B}{RECIPE_JSON_C}"
    # Dein Code kommt hier hin
