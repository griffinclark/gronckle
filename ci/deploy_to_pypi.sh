#!/bin/bash

# Exit in case of error
set -e

echo "Starting deployment to PyPI..."

# Ensure build and twine are installed
echo "Ensuring 'build' and 'twine' are installed..."
python3 -m pip install --upgrade build twine

# Clean up old dist files
echo "Cleaning up old distribution files..."
rm -rf dist/

# Build the package (both source archive and wheel)
echo "Building the package..."
python3 -m build

# Validate the package with twine
echo "Validating the package with twine..."
twine check dist/*

# Before upload, check if PYPI_API_TOKEN is set
if [ -z "$PYPI_API_TOKEN" ]; then
    echo "Error: PYPI_API_TOKEN is not set. Exiting."
    exit 1
fi

# Upload the package to PyPI using twine
echo "Uploading the package to PyPI..."
twine upload dist/* -u __token__ -p "$PYPI_API_TOKEN" --verbose

echo "Deployment to PyPI completed."
