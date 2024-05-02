# Install codecs and multimedia libraries
sudo apt install -y ubuntu-restricted-extras

# Install Microsoft TrueType core fonts
sudo apt install -y ttf-mscorefonts-installer

# Accept the EULA for the Microsoft TrueType core fonts
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | sudo debconf-set-selections

# Configure fontconfig to use the Microsoft TrueType core fonts
sudo dpkg-reconfigure fontconfig-config

# Install additional fonts
sudo apt install -y fonts-ubuntu-font-family-console fonts-open-sans fonts-roboto fonts-dejavu-core

# Install additional multimedia packages
sudo apt install -y ffmpeg gstreamer1.0-libav gstreamer1.0-plugins-ugly gstreamer1.0-plugins-bad gstreamer1.0-plugins-good

# Clean up unused packages
sudo apt autoremove

# Clear the package cache
sudo apt clean

echo "codec , fonts and media Installation complete."
