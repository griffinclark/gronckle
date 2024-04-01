#!/bin/bash

# Exit in case of error
set -e

# Check if 'build' is installed, and install it if not
if ! command -v build &> /dev/null
then
    echo "'build' could not be found, installing..."
    python3 -m pip install --upgrade build
fi

# Check if 'twine' is installed, and install it if not
if ! command -v twine &> /dev/null
then
    echo "'twine' could not be found, installing..."
    python3 -m pip install --upgrade twine
fi

# Build the package (both source archive and wheel)
python3 -m build

# Upload the package to PyPI using twine
# Use the PYPI_API_TOKEN environment variable passed from the CI server
twine upload dist/* -u __token__ -p "$PYPI_API_TOKEN"
