#!/usr/bin/env python3
import os
import sys
import requests
import click

# === CONFIG ===
PACKAGES_URL = "https://raw.githubusercontent.com/KaiPie32/stove/main/packages.json"
DOWNLOAD_DIR = os.path.expanduser("~/StoveApps")

# Make sure the download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# === CLI ===
@click.group()
def stove():
    """Stove CLI - Install and manage apps easily on macOS"""
    pass

@stove.command()
def list():
    """List available apps"""
    try:
        response = requests.get(PACKAGES_URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        click.echo(f"❌ Failed to fetch app list: {e}")
        sys.exit(1)

    click.echo("📦 Available Stove Apps:")
    for app_name in data.keys():
        click.echo(f" - {app_name}")

@stove.command()
@click.option('--app', required=True, help="App name to install")
def cook(app):
    """Install an app"""
    try:
        response = requests.get(PACKAGES_URL)
        response.raise_for_status()
        packages = response.json()
    except Exception as e:
        click.echo(f"❌ Failed to fetch app list: {e}")
        sys.exit(1)

    if app not in packages:
        click.echo(f"❌ App '{app}' not found in Stove packages.")
        sys.exit(1)

    url = packages[app]["url"]
    filename = os.path.join(DOWNLOAD_DIR, os.path.basename(url))

    click.echo(f"⬇️  Downloading {app} from {url} ...")
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        click.echo(f"✅ {app} downloaded to {filename}")
    except Exception as e:
        click.echo(f"❌ Failed to download {app}: {e}")
        sys.exit(1)

# === ENTRY POINT ===
if __name__ == "__main__":
    stove()
