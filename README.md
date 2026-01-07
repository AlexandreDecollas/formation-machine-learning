# formation-machine-learning

Practical Machine Learning training with examples and exercises.

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) for Python version management
  ```bash
  brew install pyenv  # macOS
  ```

## Quick Installation

Everything is automated! Choose your preferred method:

### Option 1: With Make (recommended)

```bash
make setup
```

### Option 2: With shell script

```bash
./setup.sh
```

### Option 3: Automatic activation with direnv (optional)

If you use [direnv](https://direnv.net/), the environment will activate automatically:

```bash
brew install direnv  # Installation (macOS)
direnv allow        # Allow the .envrc file
```

These commands will:
1. Check that pyenv is installed
2. Automatically install Python 3.12.7 if needed
3. Create the `.venv` virtual environment
4. Install all project dependencies

## Usage

> For a quick start guide, see [QUICK_START.md](QUICK_START.md)

### Activate the environment

```bash
source .venv/bin/activate
```

### Run tests

```bash
make test
```

### Other available commands

```bash
make help          # Display all available commands
make install       # Reinstall dependencies only
make dev           # Install development dependencies
make clean         # Clean virtual environment
```

## Available Python commands

Once the environment is activated, you can use:

```bash
python --version           # Check Python version
pip list                   # List installed packages
python -m ward             # Run tests
python src/path/to/file.py # Execute a script
```

## Main Dependencies

- numpy >= 2.0.0
- matplotlib >= 3.9.0
- scikit-learn >= 1.6.0
- scipy >= 1.13.0
- ward >= 0.68.0 (for testing)
