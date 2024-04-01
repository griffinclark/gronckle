#!/bin/bash

# Exit in case of error
set -e

echo "Starting deployment to PyPI..."

# Ensure all required tools are installed
echo "Installing required tools..."
python3 -m pip install --upgrade pip setuptools wheel twine build

# Clean up old dist files
echo "Cleaning up old distribution files..."
rm -rf dist/

# Build the project distributions
echo "Building the project distributions..."
python3 -m build .

# Check the distributions with twine
echo "Checking the distributions..."
twine check dist/*

# Publish the distributions to PyPI using trusted publishing setup
echo "Publishing to PyPI..."
twine upload dist/* --non-interactive --skip-existing

echo "Deployment completed successfully."
