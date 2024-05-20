import sqlite3
import json

def extract_data_from_sqlite(database_path, table_name, output_file):
    # Connect to SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Fetch data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Extract column names
    columns = [column[0] for column in cursor.description]

    # Convert data to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]

    # Write data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    # Provide the path to your SQLite database file
    sqlite_database_path = "db.sqlite3"

    # Specify the table name to extract data from
    table_to_extract = "main_app_subject"

    # Specify the output JSON file
    output_json_file = "main_app_subject.json"

    # Run the extraction script
    extract_data_from_sqlite(sqlite_database_path, table_to_extract, output_json_file)
