# Quick Start

## First Installation

Simply run:
```bash
make setup
```

That's it! This command automatically installs:
- Python 3.12.7 (via pyenv)
- The virtual environment
- All necessary dependencies

## Daily Usage

### Activate the environment
```bash
source .venv/bin/activate
```

### Run tests
```bash
make test
```

### See all available commands
```bash
make help
```

## Verify Installation

```bash
# Activate the environment
source .venv/bin/activate

# Check Python version
python --version  # Should display Python 3.12.7

# Check installed packages
pip list
```

## Common Issues

### pyenv is not installed
```bash
brew install pyenv
```

### Environment won't activate
```bash
make clean  # Clean everything
make setup  # Reinstall
```

### Dependencies won't install
```bash
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
```
