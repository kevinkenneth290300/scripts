#!/bin/bash

# Step 1: Download Firefox
echo "Downloading Firefox..."
wget -O ~/Downloads/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"

# Step 2: Extract the downloaded archive
echo "Extracting Firefox..."
tar -xvf ~/Downloads/firefox.tar.bz2 -C ~/Downloads/

# Step 3: Move Firefox to /opt/
echo "Moving Firefox to /opt/..."
sudo mv ~/Downloads/firefox /opt/

# Step 4: Create a symbolic link
echo "Creating a symbolic link..."
sudo ln -s /opt/firefox/firefox /usr/local/bin/firefox

# Step 5: Create a desktop entry
echo "Creating a desktop entry..."
cat > ~/.local/share/applications/firefox.desktop <<EOL
[Desktop Entry]
Name=Firefox
Comment=Web Browser
Exec=/opt/firefox/firefox %u
Terminal=false
Type=Application
Icon=/opt/firefox/browser/chrome/icons/default/default128.png
Categories=Network;WebBrowser;
EOL

echo "Firefox installation completed!"

