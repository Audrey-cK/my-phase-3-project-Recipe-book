from database import get_db_connection

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def create(cls, username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                       (username, password))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return cls(user_id, username, password)

    @classmethod
    def get_by_username(cls, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['username'], row['password'])
        return None

class Recipe:
    def __init__(self, id, name, ingredients, instructions, user_id):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.user_id = user_id

    @classmethod
    def create(cls, name, ingredients, instructions, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO recipes (name, ingredients, instructions, user_id) VALUES (?, ?, ?, ?)', 
                       (name, ingredients, instructions, user_id))
        conn.commit()
        recipe_id = cursor.lastrowid
        conn.close()
        return cls(recipe_id, name, ingredients, instructions, user_id)

    @classmethod
    def get_by_user_id(cls, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM recipes WHERE user_id = ?', (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['id'], row['name'], row['ingredients'], row['instructions'], row['user_id']) for row in rows]

    @classmethod
    def get_by_id(cls, recipe_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['name'], row['ingredients'], row['instructions'], row['user_id'])
        return None

    @classmethod
    def update(cls, recipe_id, name, ingredients, instructions):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('UPDATE recipes SET name = ?, ingredients = ?, instructions = ? WHERE id = ?', 
                       (name, ingredients, instructions, recipe_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, recipe_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        conn.commit()
        conn.close()

class Step:
    def __init__(self, id, description, recipe_id):
        self.id = id
        self.description = description
        self.recipe_id = recipe_id

    @classmethod
    def create(cls, description, recipe_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO steps (description, recipe_id) VALUES (?, ?)', 
                       (description, recipe_id))
        conn.commit()
        step_id = cursor.lastrowid
        conn.close()
        return cls(step_id, description, recipe_id)

    @classmethod
    def get_by_recipe_id(cls, recipe_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM steps WHERE recipe_id = ?', (recipe_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['id'], row['description'], row['recipe_id']) for row in rows]

    @classmethod
    def delete(cls, step_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM steps WHERE id = ?', (step_id,))
        conn.commit()
        conn.close()