#!/bin/bash

# Create download directory
mkdir -p ~/StoveApps

# Download stove.py
echo "⬇️  Downloading Stove CLI..."
curl -fsSL https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py -o stove

# Make it executable
chmod +x stove

# Move to /usr/local/bin so 'stove' works anywhere
sudo mv stove /usr/local/bin/stove

echo "✅ Stove CLI installed successfully!"
echo "You can now run 'stove list' and 'stove cook --app AppName'"
