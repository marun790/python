# Shopping Cart Application

A shopping cart application built with FastAPI for learning purposes. This project demonstrates building a RESTful API for managing a shopping cart system.

## 📋 Project Overview

This is a learning project to understand:
- FastAPI framework for building APIs
- RESTful API design principles
- Python project structure and dependency management
- Testing with pytest
- Code quality with ruff

## 🛠️ Tech Stack

- **Python**: ^3.12
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Logging**: Loguru
- **Testing**: pytest, pytest-cov
- **Linting**: ruff
- **Package Manager**: Poetry

## 📦 Dependencies

### Main Dependencies
- `fastapi` (>=0.128.0) - Modern web framework for building APIs
- `uvicorn` (>=0.40.0) - ASGI server for running FastAPI
- `loguru` (>=0.7.3) - Advanced logging library

### Development Dependencies
- `pytest` (>=9.0.2) - Testing framework
- `pytest-cov` (>=7.0.0) - Coverage plugin for pytest
- `ruff` (>=0.14.14) - Fast Python linter and formatter

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Poetry (for dependency management)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shoping-cart
   ```

2. **Install dependencies using Poetry**
   ```bash
   poetry install
   ```

   This will install both main and development dependencies.

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

### Running the Application

Once dependencies are installed, you can run the application:

```bash
# Using uvicorn directly
poetry run uvicorn main:app --reload

# Or activate the shell first
poetry shell
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Development Commands

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov

# Run linter
poetry run ruff check .

# Format code
poetry run ruff format .
```

## 📝 Commands Used

The following commands were used to set up this project:

### 1. Initialize Poetry Project
```bash
cd shoping-cart
poetry init
```
This command initializes a new Poetry project and creates the `pyproject.toml` file. During initialization:
- Package name: `shopping-cart`
- Version: `0.1.0`
- Description: `A shopping cart application for learning`
- Python version: `^3.12`

### 2. Add Main Dependencies
```bash
poetry add fastapi uvicorn loguru
```
This installs the core dependencies:
- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server
- `loguru` - Logging library

### 3. Add Development Dependencies
```bash
poetry add --group dev pytest pytest-cov ruff
```
This installs development tools:
- `pytest` - Testing framework
- `pytest-cov` - Coverage plugin for pytest
- `ruff` - Fast Python linter and formatter

## 📁 Project Structure

```
shoping-cart/
├── README.md           # Project documentation
├── pyproject.toml      # Project configuration and dependencies
├── poetry.lock         # Locked dependency versions
└── (project files will be added here)
```

### Planned Structure

```
shoping-cart/
├── README.md
├── pyproject.toml
├── poetry.lock
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI application entry point
│   ├── models/         # Data models
│   ├── routes/         # API routes/endpoints
│   ├── services/       # Business logic
│   └── utils/          # Utility functions
├── tests/              # Test files
│   ├── __init__.py
│   └── test_*.py
└── .env                # Environment variables (if needed)
```

## 🎯 Learning Objectives

- Understanding FastAPI framework
- Building RESTful APIs
- Managing Python dependencies with Poetry
- Writing tests with pytest
- Code quality and linting
- Project structure best practices

## 📝 Notes

This project is created for educational purposes. Feel free to experiment and learn!

## 👤 Author

Arun Chakkaravarthi M - dev.reachArun@gmail.com
