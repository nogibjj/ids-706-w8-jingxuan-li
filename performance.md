# For Rust:

1. **Table Creation (`c my_table`)**:
   - The command created a table named `my_table`.
   - Memory usage before and after the operation remained the same (0 KB).
   - The operation completed quickly, in 0.05 seconds, indicating efficient table creation without additional memory overhead.
![2681730159184_ pic](https://github.com/user-attachments/assets/6644af42-de47-4bc8-b4b4-570dd393d075)

2. **Table Deletion (`d my_table`)**:
   - The command successfully dropped the table `my_table`.
   - Memory usage before and after the operation was identical (0 KB).
   - This operation also completed swiftly in 0.04 seconds, showing that the deletion process didn’t incur any memory change or additional load.
![2691730159240_ pic](https://github.com/user-attachments/assets/1a8376f7-c40a-45db-9af5-0a2613ac432f)

3. **Data Load (`t my_table ./data/RestaurantReviews.csv`)**:
   - This command loaded data from `RestaurantReviews.csv` into `my_table`.
   - Memory usage remained unchanged before and after the operation (0 KB).
   - Execution time was 0.05 seconds, indicating that the data load was performed efficiently without impacting memory usage significantly.
![2711730159295_ pic](https://github.com/user-attachments/assets/085ba046-df8c-4629-88d3-2a707810419f)

4. **Query Execution (`q "SELECT * FROM my_table;"`)**:
   - The query retrieved all entries from `my_table`.
   - Memory usage remained constant (0 KB).
   - The command executed in 0.04 seconds, showing efficient query processing and minimal resource utilization.
![2721730159336_ pic](https://github.com/user-attachments/assets/38defd02-d24b-49fe-88b8-d3d06d13006f)


# For Python：
1. **Table Creation (`create my_table`)**:
   - The table `my_table` was successfully created.
   - **Execution Time**: 0.01 seconds, which indicates a fast creation process.
   - **Memory Usage**: 972.80 KB was used after creation, suggesting low memory consumption for this operation.

2. **Data Loading (`load my_table data/RestaurantReviews.csv`)**:
   - Data from `RestaurantReviews.csv` was loaded into `my_table`, with a total of 5 rows.
   - **Execution Time**: 0.01 seconds, indicating efficient data loading.
   - **Memory Usage**: Increased from 972.80 KB to 1104.00 KB
3. **Query Execution (`query "SELECT * FROM my_table"`)**:
   - The query successfully fetched all entries from `my_table`.
   - **Execution Time**: 0.01 seconds, showing a rapid response to retrieve the data.
   - **Memory Usage**: Increased from 1104.00 KB to 1004.00 KB

4. **Table Deletion (`delete my_table`)**:
   - The table `my_table` was deleted successfully.
   - **Execution Time**: 0.01 seconds, indicating quick cleanup.
   - **Memory Usage**: Increased slightly from 1004.00 KB to 1136.00 KB
![2671730152291_ pic](https://github.com/user-attachments/assets/1335ffa9-e4b6-454c-b800-b4e91e54330a)

# Comparison
### 1. **Execution Time Comparison**

| Operation           | Rust Execution Time | Python Execution Time |
|---------------------|---------------------|------------------------|
| **Table Creation**  | 0.05 seconds        | 0.01 seconds          |
| **Data Loading**    | 0.05 seconds        | 0.01 seconds          |
| **Query Execution** | 0.04 seconds        | 0.01 seconds          |
| **Table Deletion**  | 0.04 seconds        | 0.01 seconds          |

- **Observation**: The Python implementation consistently completes each operation in **0.01 seconds**, while the Rust implementation takes **0.04-0.05 seconds** per operation. This suggests that Python is faster for these small-scale operations, likely because of Rust's system-level safety and optimization overheads, which add some setup time.

### 2. **Memory Usage Comparison**

| Operation           | Rust Memory Change | Python Memory Usage |
|---------------------|--------------------|----------------------|
| **Table Creation**  | 0 KB               | 972.80 KB           |
| **Data Loading**    | 0 KB               | 1104.00 KB          |
| **Query Execution** | 0 KB               | 1004.00 KB          |
| **Table Deletion**  | 0 KB               | 1136.00 KB          |

- **Rust**: All operations report **0 KB memory change** before and after execution, indicating that Rust's memory handling for these database operations is optimized to avoid incremental memory allocations or deallocations. This might also suggest that Rust keeps memory usage stable and handles memory allocations upfront, especially in debug mode.
- **Python**: The memory usage in Python fluctuates slightly between operations, ranging from 972.80 KB to 1136.00 KB. This is typical for Python’s memory management, where small allocations happen dynamically as needed by the interpreter.

### Summary of Comparison
- **Execution Speed**: Python is faster for each operation at **0.01 seconds**, likely due to its high-level handling of operations without the additional safety checks that Rust includes.
- **Memory Usage Stability**: Rust shows a stable memory usage with **no changes (0 KB difference)** across all operations, which is ideal for memory consistency and might indicate that it’s managing memory allocation efficiently at the system level. Python, on the other hand, shows slight memory fluctuations, which is expected due to its garbage collection and dynamic memory allocation.

In conclusion:
- **Rust** has consistent memory usage (0 KB change) and is suitable for scenarios where memory stability is crucial.
- **Python** performs faster with minimal memory overhead, making it more efficient for lightweight, high-level tasks.
