import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def prefill_products_table(conn):
    products = [
        (1, 'B-Hydra™ Intensive Hydration Serum', 'Drunk Elephant', convertToBinaryData("./database/b-hydra-intensive-hydration-serum.jpg")),
        (2, 'Brightening Serum', 'BYOMA', convertToBinaryData("./database/brightening-serum.png")),
        (3, 'Foaming Facial Cleanser', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg")),
        (4, 'Foaming Facial Cleanser2', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg")),
        (5, 'Foaming Facial Cleanser3', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg")),
        (6, 'Foaming Facial Cleanser4', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg")),
        (7, 'Foaming Facial Cleanser5', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg")),
        (8, 'Foaming Facial Cleanser6', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg")),
        (9, 'Foaming Facial Cleanser7', 'Cerave', convertToBinaryData("./database/cerave-foaming-facial-cleanser-5_front_photo_original.jpeg"))
    ]
    
    try:
        c = conn.cursor()
        c.executemany('''
            INSERT INTO products (id, name, brand, thumbnail)
            VALUES (?, ?, ?)
        ''', products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def main():
    database = "./database/inventory.db"

    sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
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
        create_table(conn, sql_create_products_table)
        prefill_products_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()