Documentation for Inventory Management System Code:

Overview:

The code contains the implementation of an inventory management system. The system stores information about products in a database file, which is implemented using SQLite. The graphical user interface (GUI) is implemented using the Tkinter library in Python. The system has functionality to add, remove, and update product information. It also displays the products stored in the database using a Treeview widget in the GUI.

Database Connection:

To begin, the code creates a connection to the database file, inventory.db, using the sqlite3 library.

python
Copy code
db = sqlite3.connect('inventory.db')
The system then creates a table named products if it doesn't already exist in the database. The table has four columns, id, name, quantity, and price.

python
Copy code
db.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price INTEGER)')
The db.commit() method is called to commit the changes to the database and then the connection is closed using db.close().

python
Copy code
db.commit()
db.close()
Add Product Function:

The add_product() function is defined to add a new product to the database. The function takes three parameters: name, quantity, and price. Inside the function, a new connection is created to the database, and a cursor object is used to execute a SELECT statement to check if a product with the same name already exists in the database. If no matching product is found, an INSERT statement is executed to add the new product to the database, and then the connection is committed and closed. If a matching product is found, a message is printed to the console indicating that the product already exists in the database.

python
Copy code
def add_product(name, quantity, price):
db = sqlite3.connect('inventory.db')
cursor = db.cursor()
cursor.execute("SELECT name FROM products WHERE name=?", (name,))
result = cursor.fetchone()
if result is None:
cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
db.commit()
db.close()
else:
print("Product already exists in database.")
Remove Product Function:

The remove_product() function is defined to remove a product from the database based on its ID. The function takes one parameter: id. Inside the function, a new connection is created to the database, and a cursor object is used to execute a DELETE statement to remove the product from the database. The connection is then committed and closed.

python
Copy code
def remove_product(id):
db = sqlite3.connect('inventory.db')
cursor = db.cursor()
cursor.execute("DELETE FROM products WHERE id=?", (id,))
db.commit()
db.close()
Update Product Function:

The update_product() function is defined to update the information about a product in the database. The function takes four parameters: id, name, quantity, and price. Inside the function, a new connection is created to the database, and a cursor object is used to execute an UPDATE statement to update the product information in the database. The connection is then committed and closed.

python
Copy code
def update_product(id, name, quantity, price):
db = sqlite3.connect('inventory.db')
cursor = db.cursor()
cursor.execute("UPDATE products SET name=?, quantity=?, price=? WHERE id=?", (name, quantity, price, id))
db.commit()
db.close()
Display Products Function:

The display_products() function is defined to retrieve all the products stored in the database. The function creates a new connection to the database, executes
