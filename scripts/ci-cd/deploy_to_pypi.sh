#!/bin/bash

# Exit in case of error
set -e

echo "Starting deployment to PyPI..."

# Fetch the latest version of the package from PyPI
latest_version=$(pip index versions gronckle | grep -oP 'Latest version: \K(\S+)')
echo "Latest version on PyPI: $latest_version"

# Extract the current version from pyproject.toml
current_version=$(grep 'version = ' pyproject.toml | grep -oP '\K(\d+\.\d+\.\d+)')
echo "Current version in pyproject.toml: $current_version"

# Compare versions and bump if necessary
if [ "$latest_version" = "$current_version" ]; then
  IFS='.' read -ra ADDR <<< "$latest_version"
  z=${ADDR[2]}
  z=$((z+1))
  new_version="${ADDR[0]}.${ADDR[1]}.$z"
  echo "New version after bump: $new_version"
  
  # Update the version in pyproject.toml
  sed -i "s/version = \"$current_version\"/version = \"$new_version\"/" pyproject.toml
else
  echo "Current version is different from the latest on PyPI. No bump needed."
  new_version="$current_version"
fi

# Ensure all required tools are installed
echo "Installing required tools..."
python3 -m pip install --upgrade pip setuptools wheel twine build

# Clean up old dist files
echo "Cleaning up old distribution files..."
rm -rf dist/

# Build the project distributions
echo "Building the project distributions with version $new_version..."
python3 -m build .

# Check the distributions with twine
echo "Checking the distributions..."
twine check dist/*

# Publish the distributions to PyPI using trusted publishing setup
echo "Publishing to PyPI..."
twine upload dist/* --non-interactive --skip-existing

echo "Deployment completed successfully."
