# PythonSQL
Example to Teach SQL using SQLite
# Tasks
1)
- Create table: PhoneBook
fields:
- id(pk, autoincrement)
- first_name (varchar, not null)
- last_name (varchar, not null)
- phone (varchar, not null)
- age (int, not null)
- email(optional, varchar)

- Create table: Addresses
fields:
- id(pk, autoincrement)
- book_id (FK, cascade delete) --- Is FK to PhoneBook.id
- address (text)

2) 
Create Console Program with these options: 1) Insert Phonebook , 2) Edit Phonebook, 3) Delete Phonebook Entry 4) Insert Address, 5) Edit Address, 6) Delete Address 7) Delete Everything

3) Based on user input complete specified action

4) If #7 is chosen, delete the phonebook entry, then ensure that the values cascade (or are removed correctly)
