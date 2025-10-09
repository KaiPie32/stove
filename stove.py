#!/usr/bin/env python3
import os
import sys
import json
import zipfile
import requests
from pathlib import Path

PACKAGES_URL = "https://raw.githubusercontent.com/KaiPie32/stove/main/packages.json"

def get_packages():
    response = requests.get(PACKAGES_URL)
    response.raise_for_status()
    return response.json()

def download_and_extract(url, app_name):
    apps_dir = Path.home() / "Applications" / "StoveApps" / app_name
    apps_dir.mkdir(parents=True, exist_ok=True)
    temp_zip = Path.home() / f"{app_name}.zip"

    print(f"⬇️ Downloading {app_name}...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(temp_zip, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print("📦 Extracting...")
    with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
        zip_ref.extractall(apps_dir)
    temp_zip.unlink()
    print(f"✅ Installed {app_name} to {apps_dir}")

def list_apps():
    data = get_packages()
    print("📦 Available Stove Apps:")
    for app in data["apps"]:
        print(f" - {app['name']} ({app['version']})")

def cook(app_name):
    data = get_packages()
    app = next((a for a in data["apps"] if a["name"].lower() == app_name.lower()), None)
    if not app:
        print(f"❌ App '{app_name}' not found.")
        return
    download_and_extract(app["url"], app["name"])

def update():
    stove_path = Path.home() / "bin" / "stove"
    print("⬇️ Updating Stove CLI...")
    r = requests.get("https://raw.githubusercontent.com/KaiPie32/stove/main/stove.py")
    r.raise_for_status()
    stove_path.write_text(r.text)
    stove_path.chmod(0o755)
    print("✅ Stove updated successfully!")

def help():
    print("""
🍳 Stove Package Manager Commands:
  stove list              - List available apps
  stove cook --app <name> - Install an app
  stove update            - Update the CLI
  stove help              - Show this help message
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    elif sys.argv[1] == "list":
        list_apps()
    elif sys.argv[1] == "cook" and len(sys.argv) > 3 and sys.argv[2] == "--app":
        cook(sys.argv[3])
    elif sys.argv[1] == "update":
        update()
    elif sys.argv[1] == "help":
        help()
    else:
        print("❌ Invalid command. Run 'stove help' for usage.")
