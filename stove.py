import click
import json
import os
import requests

PACKAGES_URL = "https://raw.githubusercontent.com/28bm102783/StoveTop-Beta-/main/packages.json"
INSTALL_DIR = os.path.expanduser("~/StoveApps")

@click.group()
def stove():
    """🔥 Stove — your custom app installer"""
    pass

@stove.command()
@click.option('--app', required=True, help='Name of app to install')
def cook(app):
    """Install (cook) an app."""
    os.makedirs(INSTALL_DIR, exist_ok=True)
    data = requests.get(PACKAGES_URL).json()

    if app not in data:
        click.echo(f"❌ App '{app}' not found in recipe book.")
        return

    url = data[app]["url"]
    click.echo(f"🔥 Cooking up {app}...")
    os.system(f"curl -L '{url}' -o '{INSTALL_DIR}/{app}.dmg'")
    click.echo(f"✅ {app} installed to {INSTALL_DIR}")

@stove.command()
def list():
    """List available apps."""
    data = requests.get(PACKAGES_URL).json()
    click.echo("📦 Available Stove Apps:")
    for app in data.keys():
        click.echo(f" - {app}")

if __name__ == '__main__':
    stove()
