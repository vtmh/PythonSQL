import sqlite3


# ToDo
# Add validation to inputs
#

def init_tables():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS PhoneBook  ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "first_name VARCHAR NOT NULL,"
                   "last_name VARCHAR NOT NULL,"
                   "phone VARCHAR NOT NULL,"
                   "age INT NOT NULL,"
                   "email VARCHAR ) ")

    # TODO
    # This should cascade delete from book_id
    cursor.execute("CREATE TABLE IF NOT EXISTS Addresses "
                   "( id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT, book_id INTEGER,  FOREIGN KEY(book_id) REFERENCES PhoneBook(id) )")
    print("Tables successfully created and/or exist already.")


if __name__ == "__main__":
    # Create a connection to the DB
    conn = sqlite3.connect('phonebook.db')

    # Create a cursor object to perform SQL
    cursor = conn.cursor()

    # Create the phonebook table
    # if it doesn't exist already
    init_tables()

    # Ask User for Input
    print("What would you like to do?")
    print("0. Show Records")
    print("1. Insert Phonebook")
    print("2. Edit Phonebook")
    print("3. Delete Phonebook Entry")
    print("4. Insert Address")
    print("5. Edit Address")
    print("6. Delete Address")
    print("7. Delete Everything")

    user_input = input("Select your command: ")
    print(user_input)

    # Show Records
    if user_input == "0":
        print("Showing all records")
        phone_book = cursor.execute("SELECT * FROM PHONEBOOK ")

        for item in phone_book:
            print(item)

    # Add Phonebook Entry
    if user_input == "1":
        print('User has selected insert phonebook')
        # Get Fields for creating phonebook

        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        phone = input("Enter phone: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        # Insert fields into Phonebook Table
        cursor.execute('''
            INSERT INTO PHONEBOOK (first_name, last_name, phone, age, email )
            VALUES(? , ?, ?, ?, ?)
        ''',
                       (first_name, last_name, phone, age, email)
                       )
        conn.commit()

        print('Person successfully added')
    # User wants to edit the phonebook
    if user_input == "2":
        # Print out all phonebook entries
        # Allow user to choose phonebook entry
        entries = cursor.execute("SELECT * FROM PHONEBOOK")

        for entry in entries:
            print(entry)

        phonebook_id = input('Select your phonebook entry:')

        # TODO Is this the right way to select a single value?
        selection = cursor.execute("SELECT * FROM PHONEBOOK WHERE id=?", (phonebook_id))

        print('You want to edit this entry')
        print(selection.fetchall())

        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        phone = input("Enter phone: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        # Update these fields in the database
        cursor.execute(
            "UPDATE PHONEBOOK SET first_name = ?, last_name = ?, phone = ?, age = ?, email = ? WHERE id=?",
            (first_name, last_name, phone, age, email, phonebook_id))

        conn.commit()
        print("Entry updated successfully.")
