#!/bin/bash

# Uninstall Fabric if installed
pip3 uninstall -y Fabric

# Install required system packages
sudo apt-get update
sudo apt-get install -y libffi-dev libssl-dev build-essential python3.4-dev libpython3-dev

# Install required Python packages
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1

echo "All packages installed successfully!"

