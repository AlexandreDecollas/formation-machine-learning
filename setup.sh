#!/bin/bash

# Automatic installation script for formation-machine-learning
# Alternative to Makefile for those who prefer shell scripts

set -e

PYTHON_VERSION=$(cat .python-version)
VENV=".venv"

echo "🚀 Setting up machine learning training environment"
echo ""

# Check pyenv
if ! command -v pyenv &> /dev/null; then
    echo "❌ pyenv is not installed."
    echo "   Install it with: brew install pyenv"
    exit 1
fi
echo "✅ pyenv is installed"

# Check/Install Python
if ! pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then
    echo "📦 Installing Python ${PYTHON_VERSION}..."
    pyenv install ${PYTHON_VERSION}
fi
pyenv local ${PYTHON_VERSION}
echo "✅ Python ${PYTHON_VERSION} configured"

# Create virtual environment
if [ ! -d "$VENV" ]; then
    echo "🔨 Creating virtual environment..."
    python -m venv $VENV
    $VENV/bin/pip install --upgrade pip setuptools wheel
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Install dependencies
echo "📦 Installing dependencies..."
$VENV/bin/pip install -e .

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the environment:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests:"
echo "  make test"
echo "  # or: .venv/bin/python -m ward"
