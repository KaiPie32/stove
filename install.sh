#!/bin/bash

echo "🔥 Installing Stove Package Manager..."

# Create bin directory
mkdir -p "$HOME/bin"

# Download stove.py directly into bin as 'stove'
curl -fsSL https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py -o "$HOME/bin/stove"
chmod +x "$HOME/bin/stove"

# Add bin to PATH in current shell session if not present
export PATH="$HOME/bin:$PATH"

# Add to PATH permanently for zsh/bash
if ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.zshrc"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
fi
if ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
fi

echo "✅ Stove installed successfully!"
echo "You can now run 'stove list', 'stove cook --app AppName', or 'stove update'"
