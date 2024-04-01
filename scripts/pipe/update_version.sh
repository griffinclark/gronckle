#!/bin/bash

# Check Python version and import the appropriate module for loading pyproject.toml
VERSION_CODE=$(python -c "
import sys
if sys.version_info < (3, 11):
    import toml
    print(toml.load(open('pyproject.toml', 'r'))['project']['version'])
else:
    import tomllib
    print(tomllib.loads(open('pyproject.toml', 'rb').read())['project']['version'])
")

# Create or update .bumpversion.cfg with the current version
echo "Creating .bumpversion.cfg with current version $VERSION_CODE"
echo "[bumpversion]" > .bumpversion.cfg
echo "current_version = $VERSION_CODE" >> .bumpversion.cfg
echo "commit = True" >> .bumpversion.cfg
echo "tag = True" >> .bumpversion.cfg
echo "" >> .bumpversion.cfg
echo "[bumpversion:file:pyproject.toml]" >> .bumpversion.cfg
echo 'search = version = "{current_version}"' >> .bumpversion.cfg
echo 'replace = version = "{new_version}"' >> .bumpversion.cfg

# Ensure script is executable
chmod +x update_version.sh
