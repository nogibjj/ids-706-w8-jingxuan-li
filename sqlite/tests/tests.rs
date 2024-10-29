//test.rs
#[cfg(test)]
mod tests {
    // use super::*;
    use rusqlite::Connection;
    use sqlite::{create_table, drop_table, load_data_from_csv, query_exec};
    use std::fs;

    #[test]
    fn test_create_table() {
        let conn = Connection::open_in_memory().unwrap();
        let result = create_table(&conn, "test_table");
        assert!(result.is_ok());
    }

    #[test]
    fn test_query_exec() {
        let conn = Connection::open_in_memory().unwrap();
        create_table(&conn, "test_table").unwrap();
        conn.execute(
            "INSERT INTO test_table (id, restaurant, review_score, review_year) VALUES (1, 'Test Restaurant', 5, 2023)",
            [],
        )
        .unwrap();
        let result = query_exec(&conn, "SELECT * FROM test_table");
        assert!(result.is_ok());
    }

    #[test]
    fn test_drop_table() {
        let conn = Connection::open_in_memory().unwrap();
        create_table(&conn, "test_table").unwrap();
        let result = drop_table(&conn, "test_table");
        assert!(result.is_ok());
    }

    #[test]
    fn test_load_data_from_csv() {
        let conn = Connection::open_in_memory().unwrap();
        create_table(&conn, "test_table").unwrap();

        let csv_content = "1,Test Restaurant,5,2023\n2,Another Restaurant,4,2022";
        let file_path = "test_data.csv";
        fs::write(file_path, csv_content).unwrap();

        let result = load_data_from_csv(&conn, "test_table", file_path);
        assert!(result.is_ok());

        fs::remove_file(file_path).unwrap();
    }
}
