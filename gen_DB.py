import sqlite3, json

def create_database(json_data, database_name):
    # Connect to the SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Create a table to store the data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS icons (
            file_path TEXT PRIMARY KEY,
            hash TEXT,
            size INTEGER
        )
    ''')

    # Insert data into the table
    for file_path, details in json_data['objects'].items():
        hash_value = details['hash']
        size = details['size']

        cursor.execute('''
            INSERT INTO icons (file_path, hash, size)
            VALUES (?, ?, ?)
        ''', (file_path, hash_value, size))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    json_file_path = "input.json"  # Change this to the path of your JSON file
    database_name = "icon_database.db"  # Change this to the desired database name

    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    create_database(json_data, database_name)
