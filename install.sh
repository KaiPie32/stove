#!/bin/bash
echo "🔥 Installing Stove Package Manager..."

mkdir -p ~/bin
curl -fsSL https://example.com/stove.py -o ~/bin/stove.py   # Replace URL with your hosted script
chmod +x ~/bin/stove.py

# Add to PATH if not already
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
fi

echo "✅ Stove installed successfully!"
echo "Run 'stove help' to get started."
