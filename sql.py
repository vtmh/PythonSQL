import sqlite3
def fetch_into_dict(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
if __name__ == '__main__':
	# do crap with python in the main execution thread....

	# open connection with db, this will create a file

	conn = sqlite3.connect('marcus_example.db')
	print('Opened DB')

	# create table...this is just an example and should be removed when you write your real stuff
	conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL)")
	print ("Table created successfully");

	# note pks are automatically added
	conn.execute('''INSERT INTO TEST
		 (name, age)
		 VALUES('Marcus is the Man!', 30)
		 ''')
	# select that entry...
	cur = conn.execute("SELECT * FROM TEST WHERE age=?", (30,))

	# fetch everything into a dict
	list_of_dicts = fetch_into_dict(cur)

	# print it out...
	for dict in list_of_dicts:
		for key, value in dict.items():
			print(f'{key}=>{value}')

	conn.execute("DROP TABLE test")
	print('Table dropped because you are not using it...')


	conn.close()


