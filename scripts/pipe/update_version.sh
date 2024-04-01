#!/bin/bash

# Determine Python version and use appropriate module for loading pyproject.toml
VERSION_CODE=$(
python -c "
import sys
if sys.version_info < (3, 11):
    import toml  # for Python versions < 3.11
    version = toml.load(open('pyproject.toml', 'r'))['project']['version']
else:
    import tomllib  # for Python 3.11 and later
    version = tomllib.loads(open('pyproject.toml', 'rb').read())['project']['version']
print(version)
")

# Create .bumpversion.cfg with the current version
echo "Creating .bumpversion.cfg with current version $VERSION_CODE"
echo "[bumpversion]" > .bumpversion.cfg
echo "current_version = $VERSION_CODE" >> .bumpversion.cfg
echo "commit = True" >> .bumpversion.cfg
echo "tag = True" >> .bumpversion.cfg
echo "" >> .bumpversion.cfg
echo "[bumpversion:file:pyproject.toml]" >> .bumpversion.cfg
echo 'search = version = "{current_version}"' >> .bumpversion.cfg
echo 'replace = version = "{new_version}"' >> .bumpversion.cfg
