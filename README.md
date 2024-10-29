[![CI](https://github.com/nogibjj/ids-706-w7-jingxuan-li/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/ids-706-w7-jingxuan-li/actions/workflows/CI.yml)

# Rust Project Template with Functional CI/CD, Devcontainer, Dockerfile


## File Structure

- `sqlite/Makefile`: Makefile used for the `sqlite` project.
- `.github/workflows/CI.yml`: GitHub Actions CI configuration file.
- `sqlite/Cargo.toml`: Configuration file for the `sqlite` project.
- `.devcontainer/Dockerfile`: Dockerfile for setting up the development environment.
- `.devcontainer/devcontainer.json`: Devcontainer configuration file.
- `.gitignore`: Git ignore file, ignoring the `target/` directory.
- `sqlite/src/main.rs`: Main program file for the `sqlite` project.
- `sqlite/src/lib.rs`: Library file for the `sqlite` project.
- `sqlite/tests/tests.rs`: Test file for the `sqlite` project.
- `sqlite/data`: store the data file for the `sqlite` project.
## Running the Project

### Prerequisites

- Install the Rust toolchain
- Install Docker (optional)

### Using Cargo

You can use Cargo to manage the build and execution process:

1. **Install Cargo if you haven't already**
    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```
    ```bash
    cargo --version
    ```
2. **Check the Code**
    ```bash
    cargo check
    ```
3. **Build the Project**
    ```bash
    cargo build
    ```
4. **Test the Project**
    ```bash
    cargo test
    ```
5. **Format the Code**
    ```bash
    cargo fmt
    ```
6. **Lint the Code**
    ```bash
    cargo clippy
    ```
7. **Build for Release**
    ```bash
    cargo build --release
    ```


This project uses Rust to perform SQLite operations and includes CLI (Command-Line Interface) features.

See `main.rs` for a commented example of how we create our CLI. By using `clap` over standard library options (such as `std::env` for Rust or `argparse` for Python), we gain a lot of free functionality like help menu guides.

Add the compiled binary (`--release`) to your path, allowing you to use your CLI normally without needing to run:

```bash
cargo run -- -<flag> argument
```

Instead, you can use:

```bash
sqlite -c table
```

Command to add the compiled binary to the path for use:

*If in Codespaces*

```bash
export PATH=$PATH:/workspaces/<REPO_NAME>/sqlite/target/release
```


### CLI Demo
- `sqlite -c table` Create table `table1`.
- `sqlite -l table ../data/RestaurantReviews.csv` Load data into table `table` from `../data/customer_new.csv`.
- `sqlite -q "SELECT * FROM table;"` Query: `SELECT * FROM table;`
- `sqlite -d table` Drop table `table`.

### Binary Download Link
[Download Link](https://github.com/nogibjj/ids-706-w7-jingxuan-li/actions/runs/11491604094/artifacts/2096849372)

### CI/CD

The project is configured with GitHub Actions, and the CI/CD process will automatically run on every push to the `main` branch or when a pull request is submitted. The CI configuration file is located at `.github/workflows/CI.yml`.