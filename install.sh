#!/bin/bash
echo "🔥 Installing Stove Package Manager..."

mkdir -p ~/bin
curl -fsSL https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py -o ~/bin/stove.py
chmod +x ~/bin/stove.py

# Add to PATH if not already
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
fi

echo "✅ Stove installed successfully!"
echo "Run 'stove help' to get started."
