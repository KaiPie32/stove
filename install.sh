#!/bin/bash

# --- Setup directories ---
INSTALL_DIR="$HOME/bin"
APP_DIR="$HOME/StoveApps"

mkdir -p "$INSTALL_DIR"
mkdir -p "$APP_DIR"

# --- Download stove.py ---
echo "⬇️  Downloading Stove CLI..."
curl -fsSL https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py -o "$INSTALL_DIR/stove"

# --- Make executable ---
chmod +x "$INSTALL_DIR/stove"

# --- Add to PATH if not already ---
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    SHELL_CONFIG="$HOME/.zshrc"
    echo "" >> "$SHELL_CONFIG"
    echo "# Added by Stove installer" >> "$SHELL_CONFIG"
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$SHELL_CONFIG"
    source "$SHELL_CONFIG"
    echo "✅ Added $INSTALL_DIR to PATH in $SHELL_CONFIG"
fi

echo "✅ Stove CLI installed successfully!"
echo "You can now run 'stove list' and 'stove cook --app AppName'"
