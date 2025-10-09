#!/bin/bash

echo "🔥 Installing Stove Package Manager..."

# Create bin directory
mkdir -p "$HOME/bin"

# Download the main stove script
curl -fsSL https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py -o "$HOME/bin/stove"

# Make it executable
chmod +x "$HOME/bin/stove"

# Add to PATH if not already
if ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.zshrc"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
    echo "✅ Added $HOME/bin to PATH in $HOME/.zshrc"
fi

echo "✅ Stove installed successfully!"
echo ""
echo "You can now run 'stove list', 'stove cook --app AppName', or 'stove update'"
echo ""
echo "➡️  Please restart your terminal or run: source ~/.zshrc"
