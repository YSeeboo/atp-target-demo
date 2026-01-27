# ATP Target Demo

A Python testing project with pytest.

## Installation

### Using Poetry (Recommended)
```bash
# Install all dependencies including dev dependencies
poetry install

# Install only production dependencies
poetry install --only main
```

### Using pip
```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Install minimal testing dependencies (for CI/CD)
pip install -r requirements-test.txt
```

## Running Tests

### Using Poetry
```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov

# Run smoke tests only
poetry run pytest -m smoke

# Generate JSON report
poetry run pytest --json-report --json-report-file=report.json
```

### Using pytest directly
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run smoke tests only
pytest -m smoke

# Generate JSON report
pytest --json-report --json-report-file=report.json

# Run tests in parallel (requires pytest-xdist)
pytest -n auto
```

## Project Structure

```
atp-target-demo/
├── pyproject.toml          # Poetry configuration
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── requirements-test.txt   # Minimal testing dependencies
└── test_demo.py           # Test files
```

## Development

### Adding Dependencies

**Using Poetry:**
```bash
# Add production dependency
poetry add package-name

# Add dev dependency
poetry add --group dev package-name
```

**Using pip:**
Add the package to the appropriate requirements file and run:
```bash
pip install -r requirements-dev.txt
```

## Requirements Files

- **requirements.txt**: Production dependencies only
- **requirements-dev.txt**: All development dependencies (includes requirements.txt)
- **requirements-test.txt**: Minimal testing dependencies for CI/CD (includes requirements.txt)
