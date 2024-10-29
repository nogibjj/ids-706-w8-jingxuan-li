use csv::ReaderBuilder; //for loading from csv
use rusqlite::{params, Connection, Result};
use std::error::Error;
use std::fs::File; //for loading csv //for capturing errors from loading
                   // Here we will have a function for each of the commands

// Create a table
pub fn create_table(conn: &Connection, table_name: &str) -> Result<()> {
    let create_query = format!(
        "CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            restaurant TEXT NOT NULL,
            review_score INTEGER NOT NULL,
            review_year INTEGER NOT NULL
        )",
        table_name
    );
    conn.execute(&create_query, [])?;
    println!("Table '{}' created successfully.", table_name);
    Ok(()) //returns nothing except an error if it occurs
}

//Read
pub fn query_exec(conn: &Connection, query_string: &str) -> Result<()> {
    // Prepare the query and iterate over the rows returned
    let mut stmt = conn.prepare(query_string)?;

    // Use query_map to handle multiple rows
    let rows = stmt.query_map([], |row| {
        // Assuming the `users` table has an `id` and `name` column
        let id: i32 = row.get(0)?;
        let restaurant: String = row.get(1)?;
        let review_score: i32 = row.get(2)?;
        let review_year: i32 = row.get(3)?;
        Ok((id, restaurant, review_score, review_year))
    })?;

    // Iterate over the rows and print the results
    for row in rows {
        let (id, restaurant, review_score, review_year) = row?;
        println!(
            "ID: {}, Name: {}, Score: {}, Year: {}",
            id, restaurant, review_score, review_year
        );
    }

    Ok(())
}

//delete
pub fn drop_table(conn: &Connection, table_name: &str) -> Result<()> {
    let drop_query = format!("DROP TABLE IF EXISTS {}", table_name);
    conn.execute(&drop_query, [])?;
    println!("Table '{}' dropped successfully.", table_name);
    Ok(())
}

//load data from a file path to a table
pub fn load_data_from_csv(
    conn: &Connection,
    table_name: &str,
    file_path: &str,
) -> Result<(), Box<dyn Error>> {
    //Box<dyn Error> is a trait object that can represent any error type
    let file = File::open(file_path)?;
    let mut rdr = ReaderBuilder::new().from_reader(file);

    let insert_query = format!(
        "INSERT INTO {} (id, restaurant,review_score,review_year) VALUES (?, ?, ?, ?)",
        table_name
    );
    //this is a loop that expects a specific schema, you will need to change this if you have a different schema
    for result in rdr.records() {
        let record = result?;
        let id: i32 = record[0].parse()?; //.parse() is a method that converts a string into a number
        let restaurant: &str = &record[1];
        let review_score: i32 = record[2].parse()?;
        let review_year: i32 = record[3].parse()?;

        conn.execute(
            &insert_query,
            params![id, restaurant, review_score, review_year],
        )?;
    }

    println!(
        "Data loaded successfully from '{}' into table '{}'.",
        file_path, table_name
    );
    Ok(())
}
