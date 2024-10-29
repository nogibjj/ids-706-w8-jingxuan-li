import csv


def create_table(conn, table_name):
    create_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        restaurant TEXT NOT NULL,
        review_score INTEGER NOT NULL,
        review_year INTEGER NOT NULL
    )
    """
    conn.execute(create_query)
    print(f"Table '{table_name}' created successfully.")


def query_exec(conn, query_string):
    print(f"Executing query: {query_string}")
    cursor = conn.execute(query_string)
    rows = cursor.fetchall()
    print(f"Number of rows fetched: {len(rows)}")
    if not rows:
        print("No data found.")
    else:
        for row in rows:
            print(f"Result: {row}")


def drop_table(conn, table_name):
    drop_query = f"DROP TABLE IF EXISTS {table_name}"
    conn.execute(drop_query)
    print(f"Table '{table_name}' dropped successfully.")


def load_data_from_csv(conn, table_name, file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        insert_query = f"INSERT INTO {table_name} \
            (id, restaurant, review_score, review_year) VALUES (?, ?, ?, ?)"
        for row in reader:
            id, restaurant, review_score, review_year = row
            conn.execute(
                insert_query, (int(id), restaurant, int(review_score), int(review_year))
            )
    conn.commit()
