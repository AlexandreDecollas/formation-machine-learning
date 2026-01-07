.PHONY: help install setup dev clean test run

PYTHON_VERSION := $(shell cat .python-version)
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help:
	@echo "Machine Learning Training - Available commands:"
	@echo ""
	@echo "  make setup     - Complete setup (pyenv + venv + dependencies)"
	@echo "  make install   - Install dependencies only"
	@echo "  make dev       - Install with development dependencies"
	@echo "  make test      - Run tests"
	@echo "  make clean     - Clean virtual environment"
	@echo "  make run       - Activate environment (use: source .venv/bin/activate)"
	@echo ""
	@echo "Required Python version: $(PYTHON_VERSION)"

check-pyenv:
	@which pyenv > /dev/null || (echo "❌ pyenv is not installed. Install it with: brew install pyenv" && exit 1)
	@echo "✅ pyenv is installed"

check-python-version: check-pyenv
	@pyenv versions --bare | grep -q "^$(PYTHON_VERSION)$$" || \
		(echo "📦 Installing Python $(PYTHON_VERSION)..." && pyenv install $(PYTHON_VERSION))
	@pyenv local $(PYTHON_VERSION)
	@echo "✅ Python $(PYTHON_VERSION) configured"

$(VENV)/bin/activate: check-python-version
	@echo "🔨 Creating virtual environment..."
	@python -m venv $(VENV)
	@$(PIP) install --upgrade pip setuptools wheel
	@echo "✅ Virtual environment created"

setup: $(VENV)/bin/activate
	@echo "📦 Installing dependencies..."
	@$(PIP) install -e .
	@echo ""
	@echo "✅ Setup complete!"
	@echo ""
	@echo "To activate the environment:"
	@echo "  source .venv/bin/activate"

install: $(VENV)/bin/activate
	@echo "📦 Installing dependencies..."
	@$(PIP) install -e .
	@echo "✅ Installation complete!"

dev: $(VENV)/bin/activate
	@echo "📦 Installing development dependencies..."
	@$(PIP) install -e ".[dev]"
	@echo "✅ Dev installation complete!"

test:
	@echo "🧪 Running tests..."
	@$(PYTHON) -m ward

clean:
	@echo "🧹 Cleaning up..."
	@rm -rf $(VENV)
	@rm -rf *.egg-info
	@rm -rf build dist
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "✅ Cleanup complete"

run:
	@echo "To activate the environment, run:"
	@echo "  source .venv/bin/activate"
	@echo ""
	@echo "Or use directly:"
	@echo "  make test  - to run tests"
