import sqlite3
import tkinter as tk
from tkinter import ttk


# create a new database file
db = sqlite3.connect('inventory.db')

# create a table named 'products'
db.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price INTEGER)')

# commit the changes and close the database connection
db.commit()
db.close()


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



def remove_product(id):
    db = sqlite3.connect('inventory.db')
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    db.commit()
    db.close()


def update_product(id, name, quantity, price):
    db = sqlite3.connect('inventory.db')
    cursor = db.cursor()
    cursor.execute("UPDATE products SET name=?, quantity=?, price=? WHERE id=?", (name, quantity, price, id))
    db.commit()
    db.close()



def display_products():
    db = sqlite3.connect('inventory.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    db.close()
    return products


def add_product_clicked():
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    add_product(name, quantity, price)
    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    refresh_products()


def remove_product_clicked():
    id = remove_id_entry.get()
    remove_product(id)
    remove_id_entry.delete(0, tk.END)
    refresh_products()


def update_product_clicked():
    id = update_id_entry.get()
    name = update_name_entry.get()
    quantity = update_quantity_entry.get()
    price = update_price_entry.get()
    update_product(id, name, quantity, price)
    update_id_entry.delete(0, tk.END)
    update_name_entry.delete(0, tk.END)
    update_quantity_entry.delete(0, tk.END)
    update_price_entry.delete(0, tk.END)
    refresh_products()


def refresh_products():
    products = display_products()
    products_treeview.delete(*products_treeview.get_children())
    for product in products:
        products_treeview.insert('', tk.END, values=product)


app = tk.Tk()
app.title("Inventory Management System")
app.geometry("1000x700")
app.config(bg="#f0f0f0")

font1 = ('Helvetica', 12, 'bold')

# Entry fields
name_entry = tk.Entry(app, font=font1, width=30)
name_entry.place(x=150, y=20)
quantity_entry = tk.Entry(app, font=font1, width=30)
quantity_entry.place(x=150, y=60)
price_entry = tk.Entry(app, font=font1, width=30)
price_entry.place(x=150, y=100)

# Add product button
add_product_btn = tk.Button(app, text="Add Product", font=font1, command=add_product_clicked)
add_product_btn.place(x=150, y=140)

# Remove product fields and button
remove_id_entry = tk.Entry(app, font=font1, width=30)
remove_id_entry.place(x=545, y=20)
remove_product_btn = tk.Button(app, text="Remove Product", font=font1, command=remove_product_clicked)
remove_product_btn.place(x=545, y=60)

# Update product fields and button
update_id_entry = tk.Entry(app, font=font1, width=30)
update_id_entry.place(x=545, y=100)
update_name_entry = tk.Entry(app, font=font1, width=30)
update_name_entry.place(x=545, y=140)
update_quantity_entry = tk.Entry(app, font=font1, width=30)
update_quantity_entry.place(x=545, y=180)
update_price_entry = tk.Entry(app, font=font1, width=30)
update_price_entry.place(x=545, y=220)
update_product_btn = tk.Button(app, text="Update Product", font=font1, command=update_product_clicked)
update_product_btn.place(x=545, y=260)

# Display products button
display_products_btn = tk.Button(app, text="Display Products", font=font1, command=refresh_products)
display_products_btn.place(x=150, y=180)

#Products treeview
products_treeview = ttk.Treeview(app, columns=("ID", "Name", "Quantity", "Price"), show="headings", height=12)
products_treeview.place(x=50, y=350)
products_treeview.heading("ID", text="ID")
products_treeview.heading("Name", text="Name")
products_treeview.heading("Quantity", text="Quantity")
products_treeview.heading("Price", text="Price")
refresh_products()


# create labels for the text boxes
name_label = tk.Label(app, text="Name:", font=font1)
name_label.place(x=50, y=20)
quantity_label = tk.Label(app, text="Quantity:", font=font1)
quantity_label.place(x=50, y=60)
price_label = tk.Label(app, text="Price:", font=font1)
price_label.place(x=50, y=100)

# Entry fields
name_entry = tk.Entry(app, font=font1, width=30)
name_entry.place(x=150, y=20)
quantity_entry = tk.Entry(app, font=font1, width=30)
quantity_entry.place(x=150, y=60)
price_entry = tk.Entry(app, font=font1, width=30)
price_entry.place(x=150, y=100)

# Update product label
update_id_label = tk.Label(app, text="ID:", font=font1)
update_id_label.place(x=495, y=100)
update_name_label = tk.Label(app, text="Name:", font=font1)
update_name_label.place(x=485, y=140)
update_quantity_label = tk.Label(app, text="Quantity:", font=font1)
update_quantity_label.place(x=465, y=180)
update_price_label = tk.Label(app, text="Price:", font=font1)
update_price_label.place(x=485, y=220)

# Remove product label
remove_id_label = tk.Label(app, text="ID:", font=font1)
remove_id_label.place(x=495, y=20)


app.mainloop()
