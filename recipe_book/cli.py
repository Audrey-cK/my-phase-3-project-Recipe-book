#!/usr/bin/env python3

from database import init_db
from models import User, Recipe, Step

def print_main_menu():
    print("\nRecipe Book Manager")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def print_user_menu():
    print("\nUser Menu")
    print("1. Add a new recipe")
    print("2. Add a step to a recipe")
    print("3. Update a recipe")
    print("4. Delete a recipe")
    print("5. View all my recipes")
    print("6. View a single recipe by ID")
    print("7. View steps of a recipe")
    print("8. Logout")

def main():
    init_db()
    current_user = None
    
    while True:
        if current_user is None:
            print_main_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                User.create(username, password)
                print(f"User {username} registered successfully!")

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User.get_by_username(username)
                if user and user.password == password:
                    current_user = user
                    print(f"User {username} logged in successfully!")
                else:
                    print("Invalid username or password")

            elif choice == '3':
                print("Exiting...")
                break

            else:
                print("Invalid choice, please try again.")
        else:
            print_user_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter recipe name: ")
                ingredients = input("Enter ingredients (comma separated): ")
                instructions = input("Enter instructions: ")
                Recipe.create(name, ingredients, instructions, current_user.id)
                print("Recipe added successfully!")

            elif choice == '2':
                recipe_id = int(input("Enter recipe ID to add step to: "))
                description = input("Enter step description: ")
                Step.create(description, recipe_id)
                print("Step added successfully!")

            elif choice == '3':
                recipe_id = int(input("Enter recipe ID to update: "))
                name = input("Enter new name (or leave blank to keep current): ")
                ingredients = input("Enter new ingredients (or leave blank to keep current): ")
                instructions = input("Enter new instructions (or leave blank to keep current): ")
                recipe = Recipe.get_by_id(recipe_id)
                if recipe and recipe.user_id == current_user.id:
                    if not name:
                        name = recipe.name
                    if not ingredients:
                        ingredients = recipe.ingredients
                    if not instructions:
                        instructions = recipe.instructions
                    Recipe.update(recipe_id, name, ingredients, instructions)
                    print("Recipe updated successfully!")
                else:
                    print("Recipe not found or you don't have permission to update it")

            elif choice == '4':
                recipe_id = int(input("Enter recipe ID to delete: "))
                recipe = Recipe.get_by_id(recipe_id)
                if recipe and recipe.user_id == current_user.id:
                    Recipe.delete(recipe_id)
                    print("Recipe deleted successfully!")
                else:
                    print("Recipe not found or you don't have permission to delete it")

            elif choice == '5':
                recipes = Recipe.get_by_user_id(current_user.id)
                for recipe in recipes:
                    print(f"ID: {recipe.id}, Name: {recipe.name}\nIngredients: {recipe.ingredients}\nInstructions: {recipe.instructions}\n")

            elif choice == '6':
                recipe_id = int(input("Enter recipe ID to view: "))
                recipe = Recipe.get_by_id(recipe_id)
                if recipe and recipe.user_id == current_user.id:
                    print(f"ID: {recipe.id}, Name: {recipe.name}\nIngredients: {recipe.ingredients}\nInstructions: {recipe.instructions}")
                else:
                    print("Recipe not found or you don't have permission to view it")

            elif choice == '7':
                recipe_id = int(input("Enter recipe ID to view steps: "))
                steps = Step.get_by_recipe_id(recipe_id)
                for step in steps:
                    print(f"Step ID: {step.id}, Description: {step.description}")
                    
            elif choice == '8':
                current_user = None
                print("Logged out successfully!")

            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
