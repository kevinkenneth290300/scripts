#!/bin/bash

#install cUrl
sudo apt install curl
# Install Node.js and npm
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs

# Check Node.js and npm versions
node -v
npm -v

# Uninstall global Cypress package
sudo npm uninstall -g cypress

# Install specific version of Cypress
sudo npm i -g cypress@9.7.0

# Install Cypress as a development dependency
npm install --save-dev cypress

# Install all dependencies
npm install

echo "Installation complete."

