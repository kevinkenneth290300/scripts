#!/bin/bash

# Update and upgrade system
sudo apt update
sudo apt upgrade -y

# Install Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt update
sudo apt install google-chrome-stable -y

# Install Slack
wget https://downloads.slack-edge.com/linux_releases/slack-desktop-4.32.2-amd64.deb
sudo dpkg -i slack-desktop-4.19.2-amd64.deb
sudo apt --fix-broken install -y

# Install Postman
sudo snap install postman

# Install Postbird
sudo snap install postbird

# Install PostgreSQL
sudo apt install postgresql -y

# Install GoLand
sudo snap install goland --classic

# Install WebStorm
sudo snap install webstorm --classic

# Install Go 1.9.5
wget https://dl.google.com/go/go1.20.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.20.5.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Install Node.js and NVM
#curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
#source ~/.bashrc
#nvm install node

#install git
sudo apt install git
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

echo " cypress Installation complete."

# Install IntelliJ IDEA
sudo snap install intellij-idea-ultimate --classic

# Install SimpleScreenRecorder
sudo apt-get install simplescreenrecorder

# Install Flameshot
sudo apt-get install flameshot

# Install Wireshark
sudo apt-get install wireshark
sudo usermod -aG wireshark $USER
sudo chgrp $USER /usr/bin/dumpcap
sudo chmod 750 /usr/bin/dumpcap

# Install DBeaver
wget -O - https://dbeaver.io/debs/dbeaver.gpg.key | sudo apt-key add -
echo "deb https://dbeaver.io/debs/dbeaver-ce /" | sudo tee /etc/apt/sources.list.d/dbeaver.list
sudo apt update
sudo apt-get install dbeaver-ce

# Install VLC
sudo apt-get install vlc

# Install WPS Office
#wget -O wps-office.deb https://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/10702/wps-office_11.1.0.10702.XA_amd64.deb
#sudo dpkg -i wps-office.deb
#sudo apt --fix-broken install -y

# Install Whatsdesk
sudo snap install whatsdesk

echo "Software installation complete."

# Update and upgrade system
sudo apt update
sudo apt upgrade -y

# Install TLP for power management
sudo apt install tlp tlp-rdw -y
sudo tlp start

# Adjust swappiness
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Disable unnecessary startup applications
#mkdir -p ~/.config/autostart
#mv ~/.config/autostart/* /tmp  # Move existing startup applications to temporary folder

# Install Preload for application optimization
sudo apt install preload -y

# Use a lightweight desktop environment (e.g., Xfce)
# Uncomment the following lines if you want to install Xfce
# sudo apt install xfce4 -y
# echo "exec xfce4-session" >> ~/.xinitrc

# Disable visual effects (comment out if not desired)
gsettings set org.gnome.desktop.interface enable-animations false

# Keep the system updated
sudo apt update
sudo apt upgrade -y

echo "System performance optimization complete."

#!/bin/bash

# Remove the default Firefox browser
sudo apt remove firefox -y

# Download Firefox Nightly from the official website
wget -O firefox-nightly.tar.bz2 "https://download.mozilla.org/?product=firefox-nightly-latest-ssl&os=linux64&lang=en-US"

# Extract the downloaded archive
tar -xvf firefox-nightly.tar.bz2

# Move Firefox Nightly to the /opt directory
sudo mv firefox /opt/firefox-nightly
# Create a symbolic link for easier access
sudo ln -s /opt/firefox-nightly/firefox /usr/local/bin/firefox-nightly
# Create a desktop entry for Firefox Nightly
cat > ~/.local/share/applications/firefox-nightly.desktop <<EOL
[Desktop Entry]
Name=Firefox Nightly
Exec=/opt/firefox-nightly/firefox %u
Icon=/opt/firefox-nightly/browser/chrome/icons/default/default128.png
Terminal=false
Type=Application
Categories=Network;WebBrowser;
EOL
# Clean up the downloaded archive
rm firefox-nightly.tar.bz2
echo "Firefox Nightly has been installed successfully!"

# Download Go
wget https://golang.org/dl/go1.19.5.linux-amd64.tar.gz
# Extract the contents
sudo tar -xvf go1.19.5.linux-amd64.tar.gz
# Move the extracted directory to /usr/local
sudo mv go /usr/local
# Edit the .zshrc file
vim ~/.zshrc
# Add environment variables
echo 'export GOPATH=$HOME/go' >> ~/.zshrc
echo 'export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin' >> ~/.zshrc
# Load the settings into the shell
source ~/.zshrc
# Check the Go version
go version

# Install GitHub Desktop
echo "Installing GitHub Desktop..."
wget -O github-desktop.deb https://github.com/shiftkey/desktop/releases/download/release-2.10.1-linux1/GitHubDesktop-linux-2.10.1-linux1.deb
sudo dpkg -i github-desktop.deb
sudo apt install -f -y
rm github-desktop.deb

# Install LibreOffice
echo "Installing LibreOffice..."
sudo apt install libreoffice -y

echo "Installing necessary Fonts and Multimedia Packages"
# Update the package lists
sudo apt update

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

# Install additional utility packages
#sudo apt install -y unzip p7zip-full

# Clean up unused packages
sudo apt autoremove -y

# Clear the package cache
sudo apt clean

echo "Installation of Fonts and Multimedia packages complete."

# Update and upgrade system
sudo apt update
sudo apt upgrade -y

# Install TLP for power management
sudo apt install tlp tlp-rdw -y
sudo tlp start

# Adjust swappiness
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Disable unnecessary startup applications
mkdir -p ~/.config/autostart
mv ~/.config/autostart/* /tmp  # Move existing startup applications to temporary folder

# Install Preload for application optimization
sudo apt install preload -y

# Use a lightweight desktop environment (e.g., Xfce)
# Uncomment the following lines if you want to install Xfce
# sudo apt install xfce4 -y
# echo "exec xfce4-session" >> ~/.xinitrc

# Disable visual effects (comment out if not desired)
gsettings set org.gnome.desktop.interface enable-animations false

# Keep the system updated
sudo apt update
sudo apt upgrade -y

echo "System performance optimization complete."

