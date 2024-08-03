import sqlite3

# Function to read data from the SQLite database
def read_data_from_db(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a SELECT query to fetch all data from the 'people' table
    cursor.execute('SELECT * FROM people')

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Return the fetched data
    return rows

# Define the path to the SQLite database
db_path = '/Users/peternyman/Clips/outlook.db'

# Read data from the database
data = read_data_from_db(db_path)

# Print the fetched data
for row in data:
    total = ""
    for item in row:
        total += str(item) + "¤"
    print(total)
