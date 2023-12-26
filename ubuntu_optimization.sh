#!/bin/bash

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

