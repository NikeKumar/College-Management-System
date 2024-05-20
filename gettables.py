import sqlite3

def get_table_names(database_path):
    # Connect to SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Query to get table names from sqlite_master
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    # Fetch all table names
    table_names = cursor.fetchall()

    # Close the connection
    connection.close()

    return table_names

if __name__ == "__main__":
    # Provide the path to your SQLite database file
    sqlite_database_path = "db.sqlite3"

    # Get table names
    tables = get_table_names(sqlite_database_path)

    # Print the table names
    print("Tables in the SQLite database:")
    for table in tables:
        print(table[0])
