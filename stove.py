import os
import sys
import json
import zipfile
import requests
from pathlib import Path

def get_packages():
    url = "https://raw.githubusercontent.com/KaiPie32/stove/main/packages.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_and_extract(url, app_name):
    apps_dir = Path.home() / "Applications" / "StoveApps" / app_name
    apps_dir.mkdir(parents=True, exist_ok=True)

    temp_zip = Path.home() / f"{app_name}.zip"

    print(f"⬇️ Downloading {app_name}...")
    response = requests.get(url, stream=True)
    with open(temp_zip, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print("📦 Extracting...")
    with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
        zip_ref.extractall(apps_dir)

    temp_zip.unlink()  # delete zip after extraction
    print(f"✅ Installed {app_name} to {apps_dir}")

def cook(app_name):
    packages = get_packages()
    app = next((p for p in packages["apps"] if p["name"].lower() == app_name.lower()), None)
    if not app:
        print(f"❌ App '{app_name}' not found.")
        return
    download_and_extract(app["url"], app["name"])

def list_apps():
    packages = get_packages()
    print("📦 Available apps:")
    for app in packages["apps"]:
        print(f"- {app['name']} ({app['version']})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: stove [list|cook --app AppName]")
    elif sys.argv[1] == "list":
        list_apps()
    elif sys.argv[1] == "cook" and len(sys.argv) > 3 and sys.argv[2] == "--app":
        cook(sys.argv[3])
    else:
        print("Invalid command.")
