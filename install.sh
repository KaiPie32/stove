#!/bin/bash
echo "🔥 Installing Stove Package Manager..."

# Create bin directory
mkdir -p "$HOME/bin"

# Download CLI
curl -fsSL https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py -o "$HOME/bin/stove"
chmod +x "$HOME/bin/stove"

# Add ~/bin to PATH in current shell session
export PATH="$HOME/bin:$PATH"

# Add to PATH permanently
if [ -f "$HOME/.zshrc" ] && ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.zshrc"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
fi
if [ -f "$HOME/.bashrc" ] && ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
fi

echo "✅ Stove installed successfully!"
echo "Run 'stove help' to get started."
