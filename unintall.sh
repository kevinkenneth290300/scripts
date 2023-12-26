#!/bin/bash

# Remove IntelliJ IDEA
rm -rf $HOME/idea-IC-2023.1.3

# Remove GoLand
rm -rf $HOME/goland-2023.1.3

# Remove WebStorm
rm -rf $HOME/webstorm-2023.1.3

# Remove application icons
rm $HOME/.local/share/applications/intellij-idea.desktop
rm $HOME/.local/share/applications/goland.desktop
rm $HOME/.local/share/applications/webstorm.desktop

echo "IntelliJ IDEA, GoLand, and WebStorm have been uninstalled."


