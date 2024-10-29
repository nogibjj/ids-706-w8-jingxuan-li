import argparse
import sqlite3
from mylib.lib import create_table, query_exec, drop_table, load_data_from_csv
import time
import psutil


def main():
    start_time = time.time()
    parser = argparse.ArgumentParser(description="SQLite CLI tool")
    subparsers = parser.add_subparsers(dest="command")
    process = psutil.Process()
    start_memory = process.memory_info().rss

    # Create command
    create_parser = subparsers.add_parser(
        "create", aliases=["c"], help="Create a table"
    )
    create_parser.add_argument(
        "table_name", type=str, help="Name of the table to create"
    )

    # Query command
    query_parser = subparsers.add_parser("query", aliases=["q"], help="Execute a query")
    query_parser.add_argument("query", type=str, help="SQL query to execute")

    # Delete command
    delete_parser = subparsers.add_parser(
        "delete", aliases=["d"], help="Delete a table"
    )
    delete_parser.add_argument(
        "delete_query", type=str, help="Name of the table to delete"
    )

    # Load command
    load_parser = subparsers.add_parser(
        "load", aliases=["l"], help="Load data from CSV"
    )
    load_parser.add_argument(
        "table_name", type=str, help="Name of the table to load data into"
    )
    load_parser.add_argument("file_path", type=str, help="Path to the CSV file")

    args = parser.parse_args()

    conn = sqlite3.connect("my_database.db")

    if args.command in ["create", "c"]:
        print(f"Creating Table {args.table_name}")
        create_table(conn, args.table_name)

    elif args.command in ["query", "q"]:
        print(f"Query: {args.query}")
        query_exec(conn, args.query)

    elif args.command in ["delete", "d"]:
        print(f"Deleting: {args.delete_query}")
        drop_table(conn, args.delete_query)

    elif args.command in ["load", "l"]:
        print(f"Loading data into table '{args.table_name}' from '{args.file_path}'")
        load_data_from_csv(conn, args.table_name, args.file_path)
        cursor = conn.execute(f"SELECT * FROM {args.table_name}")

        rows = cursor.fetchall()
        print(f"Number of rows in {args.table_name} after loading: {len(rows)}")
        for row in rows:
            print(row)

    conn.close()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")

    end_memory = process.memory_info().rss

    print(f"Memory usage: {(end_memory - start_memory) / 1024:.2f} KB")


if __name__ == "__main__":
    main()

# python3 main.py create my_table
# python3 main.py load my_table data/RestaurantReviews.csv
# python3 main.py query "SELECT * FROM my_table"
# python3 main.py delete my_table
