# Recipe Book Manager

Recipe Book Manager is a Python CLI application that allows users to manage their recipes. Users can register, log in, add recipes, add steps to recipes, update recipes, delete recipes, and view their recipes.

## Features

- **User Management**: Register, log in, and delete users.
- **Recipe Management**: Create, update, delete, and view recipes.
- **Step Management**: Add and view steps for recipes.
- **Database**: Uses SQLite for storing user, recipe, and step data.

## Requirements

- Python 3.x
- SQLite

## Installation

1. **Clone the repository**:
   ```bash
   git@github.com:Audrey-cK/my-phase-3-project-Recipe-book.git
   cd my-phase-3-project-Recipe-book 
2. **Create a virtual environment and activate it**:
   ```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies**:
```bash
pip install -r requirements.txt
Initialize the database:
The database will be initialized automatically when you run the application for the first time.

- **Usage**
Run the application:

```bash
python cli.py
Main Menu Options:

Register: Create a new user account.
Login: Log in to an existing user account.
Delete User: Delete a user account.
Exit: Exit the application.
User Menu Options (after logging in):

Add a new recipe: Create a new recipe.
Add a step to a recipe: Add a step to an existing recipe.
Update a recipe: Update details of an existing recipe.
Delete a recipe: Delete an existing recipe.
View all my recipes: View all recipes created by the logged-in user.
View a single recipe by ID: View details of a specific recipe by its ID.
View steps of a recipe: View all steps of a specific recipe by its ID.
Logout: Log out of the current user account.
Example
Here is a simple example of how to use the application:

Register a new user:


Recipe Book Manager
1. Register
2. Login
3. Delete User
4. Exit
Enter your choice: 1
Enter username: testuser
Enter password: password123
User testuser registered successfully!
Log in:


Recipe Book Manager
1. Register
2. Login
3. Delete User
4. Exit
Enter your choice: 2
Enter username: testuser
Enter password: password123
User testuser logged in successfully!
Add a new recipe:


User Menu
1. Add a new recipe
2. Add a step to a recipe
3. Update a recipe
4. Delete a recipe
5. View all my recipes
6. View a single recipe by ID
7. View steps of a recipe
8. Logout
Enter your choice: 1
Enter recipe name: Pancakes
Enter ingredients (comma separated): Flour, Eggs, Milk
Enter instructions: Mix all ingredients and cook on a griddle.
Recipe added successfully!
View all recipes:


User Menu
1. Add a new recipe
2. Add a step to a recipe
3. Update a recipe
4. Delete a recipe
5. View all my recipes
6. View a single recipe by ID
7. View steps of a recipe
8. Logout
Enter your choice: 5
ID: 1, Name: Pancakes
Ingredients: Flour, Eggs, Milk
Instructions: Mix all ingredients and cook on a griddle.
Project Structure
database.py: Contains functions for initializing and connecting to the SQLite database.
models.py: Contains the data models for User, Recipe, and Step.
cli.py: Contains the CLI logic for interacting with the user.
test_script.py: Contains test scripts to verify the functionality of the application (optional).

## Contribution

- **Contributions**: are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

