class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def display_recipes(self):
        for i, recipe in enumerate(self.recipes, 1):
            print(f"{i}. {recipe.name}")

    def get_recipe(self, index):
        return self.recipes[index - 1]

def main():
    manager = RecipeManager()

    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter instructions: ")
            recipe = Recipe(name, ingredients, instructions)
            manager.add_recipe(recipe)
            print("Recipe added successfully!")

        elif choice == "2":
            manager.display_recipes()
            if manager.recipes:
                index = int(input("Enter the number of the recipe to view details: "))
                recipe = manager.get_recipe(index)
                print(f"\nRecipe: {recipe.name}")
                print("Ingredients:")
                for ingredient in recipe.ingredients:
                    print(f"- {ingredient.strip()}")
                print(f"Instructions: {recipe.instructions}")
            else:
                print("No recipes available.")

        elif choice == "3":
            print("Thank you for using Recipe Manager!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()