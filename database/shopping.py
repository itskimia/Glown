import sqlite3

from inventory import create_connection, create_table

database = "./database/shopping_bag.db"

def getProductNames(create_table_sql):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Retrieve product names
    cursor.execute('SELECT name FROM shopping_products')
    product_names = cursor.fetchall()

    # Print product names
    for name in product_names:
        print(name[0])

    # Close the connection
    conn.close()

def addProductToShopping(product):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    sql_create_shopping_products_table = """ CREATE TABLE IF NOT EXISTS shopping_products (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    brand text NOT NULL,
                                    thumbnail BLOB NOT NULL UNIQUE
                                ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_shopping_products_table)
        # add to database
        cursor.executemany('''
            INSERT INTO products (id, name, brand, thumbnail)
            VALUES (?, ?, ?)
        ''', product)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")
