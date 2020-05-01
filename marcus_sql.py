import sqlite3

if __name__ == "__main__":
    print('hello')

    #Create a connection to the DB
    conn = sqlite3.connect('phonebook.db')

    #Create a cursor object to perform SQL
    cursor = conn.cursor()

    #Create the phonebook table
    cursor.execute("CREATE TABLE PhoneBook ( "
                   "id INTEGER PRIMARY KEY"
                   "first_name VARCHAR NOT NULL"
                   "last_name VARCHAR NOT NULL"
                   "phone VARCHAR NOT NULL"
                   "age INT NOT NULL"
                   "email VARCHAR"
                   ") ")

    print("Table succeessfully made")





