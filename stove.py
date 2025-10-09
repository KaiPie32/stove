#Fixed Script I Think
#!/usr/bin/env python3
import os
import sys
import urllib.request
import zipfile
import shutil
from pathlib import Path
import subprocess

# =========================
# CONFIGURATION
# =========================
INSTALL_DIR = Path.home() / "Applications/StoveApps"
STOVE_PATH = Path.home() / "bin" / "stove.py"
PACKAGE_REPO = "https://raw.githubusercontent.com/KaiPie32/stove/refs/heads/main/packages.json"  
STOVE_SCRIPT_URL = "https://raw.githubusercontent.com/KaiPie32/stove/refs/heads/main/stove.py"

# =========================
# CORE FUNCTIONS
# =========================
def ensure_install_dir():
    INSTALL_DIR.mkdir(parents=True, exist_ok=True)

def install(package_name):
    ensure_install_dir()
    package_url = f"{PACKAGE_REPO}/{package_name}.zip"
    package_path = INSTALL_DIR / f"{package_name}.zip"

    print(f"📦 Downloading {package_name} from {package_url}...")
    try:
        urllib.request.urlretrieve(package_url, package_path)
    except Exception as e:
        print(f"❌ Failed to download {package_name}: {e}")
        return

    print("📂 Unpacking package...")
    try:
        with zipfile.ZipFile(package_path, "r") as zip_ref:
            zip_ref.extractall(INSTALL_DIR / package_name)
    except Exception as e:
        print(f"❌ Failed to unpack {package_name}: {e}")
        return

    package_path.unlink()
    print(f"✅ Installed {package_name} in {INSTALL_DIR}/{package_name}")

def list_installed():
    ensure_install_dir()
    apps = [p.name for p in INSTALL_DIR.iterdir() if p.is_dir()]
    if not apps:
        print("📭 No packages installed.")
    else:
        print("📦 Installed packages:")
        for app in apps:
            print(f" - {app}")

def uninstall(package_name):
    path = INSTALL_DIR / package_name
    if path.exists():
        shutil.rmtree(path)
        print(f"🗑️  Uninstalled {package_name}")
    else:
        print(f"❌ {package_name} not found.")

def update():
    print("🔄 Updating Stove package manager...")
    try:
        urllib.request.urlretrieve(STOVE_SCRIPT_URL, STOVE_PATH)
        os.chmod(STOVE_PATH, 0o755)
        print("✅ Stove has been updated successfully!")
    except Exception as e:
        print(f"❌ Update failed: {e}")

def help_menu():
    print("""
Stove Package Manager

Usage:
  stove install <package>     Install a package
  stove list                  List installed packages
  stove uninstall <package>   Uninstall a package
  stove update                Update Stove
  stove help                  Show this help message
""")

def main():
    if len(sys.argv) < 2:
        help_menu()
        return

    command = sys.argv[1]

    if command == "install" and len(sys.argv) == 3:
        install(sys.argv[2])
    elif command == "list":
        list_installed()
    elif command == "uninstall" and len(sys.argv) == 3:
        uninstall(sys.argv[2])
    elif command == "update":
        update()
    elif command == "help":
        help_menu()
    else:
        help_menu()

if __name__ == "__main__":
    main()
