import sqlite3


# ToDo
# Add validation to inputs
# Is there a less annoying way to write queries?
# Try again to add validation

def show_book():
    phone_book = cursor.execute("SELECT * FROM PHONEBOOK ")

    for item in phone_book:
        print(item)

def show_addresses():
    selected_table = cursor.execute("SELECT * FROM ADDRESSES")

    for item in selected_table:
        print(item)

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
                   "( id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT, book_id INTEGER,  FOREIGN KEY(book_id) REFERENCES PhoneBook(id) ON DELETE CASCADE )")
    print("Tables successfully created and/or exist already.")


if __name__ == "__main__":
    # Create a connection to the DB
    conn = sqlite3.connect('phonebook.db')



    # Create a cursor object to perform SQL
    cursor = conn.cursor()

    #Enable foreign keys
    print(cursor.execute('PRAGMA foreign_keys = ON'))

    # Create the phonebook table
    # if it doesn't exist already
    init_tables()

    # print(cursor.execute('PRAGMA foreign_keys').fetchall())
    # print(cursor.execute('pragma table_info(Addresses)').fetchall())

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
        email = input("Enter email: " or None)

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
        # Grab all phonebook entries
        entries = cursor.execute("SELECT * FROM PHONEBOOK")

        # Print out all phonebook entries
        for entry in entries:
            print(entry)

        phonebook_id = input('Select your phonebook entry:')

        # TODO Is this the right way to select a single value?
        selection = cursor.execute("SELECT * FROM PHONEBOOK WHERE id=?", (phonebook_id))

        print('Selected Entry: ')
        for entry in selection:
            print(entry)

        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        phone = input("Enter phone: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        # Update these fields in the database
        cursor.execute(
            "UPDATE PHONEBOOK SET first_name = ?, last_name = ?, phone = ?, age = ?, email = ? WHERE id=?",
            (first_name, last_name, phone, age, email, phonebook_id))

        #commit change
        conn.commit()
        print("Entry updated successfully.")

    #Delete a phonebook entry
    if user_input == "3":
        print("Choose an entry to delete")
        selection = cursor.execute("SELECT * FROM PhOnEboOk")
        print(selection.fetchall())
        deleted_entry = input("Delete this Entry:  ")
        cursor.execute("DELETE FROM PHONEBOOK WHERE id=?", (deleted_entry))
        conn.commit()

        print('Entry successfully deleted')


    #Insert Address
    if user_input == "4":

        print("Which entry is this for?")
        show_book()

        phonebook_entry = input("Add address to this entry: ")
        print("Create a new address")
        address = input("Enter an address: ")
        print(address)
        #Insert the address
        cursor.execute('INSERT into Addresses (address, book_id) VALUES (?, ?)', (address, phonebook_entry))

        conn.commit()

    #Edit Address
    if user_input == "5":
        #print out book
        show_addresses()

        address_id = input('Select your address entry:')

        selection = cursor.execute("SELECT * FROM ADDRESSES WHERE id=?", (address_id))

        print('Selected Address: ')
        print(selection.fetchall())
        edited_address = input("Enter an address: ")

        # Update these fields in the database
        cursor.execute(
            "UPDATE ADDRESSES SET address = ? WHERE id=?",
            (edited_address, address_id,))

        # commit change
        conn.commit()
        print("Address updated successfully.")

    #Delete Address
    if user_input == "6":
        print("Choose an address to delete")
        selection = cursor.execute("SELECT * FROM ADDRESSES")
        print(selection.fetchall())
        deleted_address = input("Delete this Entry:  ")
        cursor.execute("DELETE FROM ADDRESSES WHERE id=?", (deleted_address))
        conn.commit()

        print('Address successfully deleted')

    #Delete Everything
    if user_input == "7":

        user_choice = input("Are you sure you want to delete everything? [Y/N]")

        if user_choice == "Y":
            # print('DELETED')
            # grab all phonebook
            entries = cursor.execute("SELECT * FROM PHONEBOOK")
            # print(entries.fetchall())

            cursor.execute("DELETE FROM PHONEBOOK")
            conn.commit()

            #loop through and delete
            # for entry in entries:
            #     print(entry)
            #     #entry must be converted to string
            #     entry_id = str(entry[0])
            #     print(entry_id)
            #     cursor.execute("DELETE FROM PHONEBOOK WHERE id=?", (entry_id))
            #     print('Deleted: ', entry)



        if user_choice == "N":
            print("Operation Aborted")
