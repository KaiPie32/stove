#!/bin/bash

echo "⬇️  Downloading Stove CLI..."

# Create bin folder in user's home
mkdir -p "$HOME/bin"

# Download the Stove executable script
curl -fsSL "https://raw.githubusercontent.com/KaiPie32/stove/main/stove" -o "$HOME/bin/stove"
chmod +x "$HOME/bin/stove"

# Add $HOME/bin to PATH if not already
if ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.zshrc"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
    echo "✅ Added $HOME/bin to PATH in $HOME/.zshrc"
fi

echo "✅ Stove CLI installed successfully!"
echo ""
echo "👉 Restart your terminal or run: source ~/.zshrc"
echo "Then use 'stove list' or 'stove install <app>'"
