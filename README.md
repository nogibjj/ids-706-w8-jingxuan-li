[![RustCI](https://github.com/nogibjj/ids-706-w8-jingxuan-li/actions/workflows/RustCI.yml/badge.svg)](https://github.com/nogibjj/ids-706-w8-jingxuan-li/actions/workflows/RustCI.yml)
[![Python CI](https://github.com/nogibjj/ids-706-w8-jingxuan-li/actions/workflows/PythonCI.yml/badge.svg)](https://github.com/nogibjj/ids-706-w8-jingxuan-li/actions/workflows/PythonCI.yml)
# Rewrite Python in Rust with Functional CI/CD, Devcontainer, Dockerfile


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
- `main.py`: Main program file for the python project.
- `mylib/lib.py`: Library file for the python project.
- `test_main.py`: Test file for the python project.
- `requirement.txt`: requirement library for the python project
## Running the Rust Project

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
[Download Link](https://github.com/nogibjj/ids-706-w8-jingxuan-li/actions/runs/11564723325/artifacts/2115146320)


## Running the Python Project


## Prerequisites
- Python 3.x
- pip
- Docker (for containerized code linting)

## Install Dependencies
Run the following command in the root directory of the project to install the required Python packages:

```bash
make install
```

## Run Tests
Use the following command to run tests and generate a code coverage report:

```bash
make test
```

## Format Code
Format Python code using `black`:

```bash
make format
```

## Lint Code
Perform fast code linting using `ruff`:

```bash
make lint
```

## Containerized Code Linting
Check the Dockerfile using `hadolint`:

```bash
make container-lint
```

## Refactor Code
Run both formatting and linting:

```bash
make refactor
```

## Run All
Perform installation, linting, testing, and formatting:

```bash
make all
```

## Generate and Push Changes
Generate a Markdown file and push changes to GitHub:

```bash
make generate_and_push
```

## Notes
- Ensure Git is properly configured and you have push permissions before running `generate_and_push`.
- The `generate_and_push` command will automatically commit and push changes to GitHub.
```



### CI/CD

The project is configured with GitHub Actions, and the CI/CD process will automatically run on every push to the `main` branch or when a pull request is submitted. The CI configuration file for Rust project is located at `.github/workflows/RustCI.yml`, and for python project is located at:`.github/workflows/PythonI.yml