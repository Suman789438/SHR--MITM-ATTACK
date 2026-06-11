#!/usr/bin/env python3
"""
Automated Package Installer for HCO-MITM Framework
Supports Termux & Linux (Debian/Ubuntu/Kali)
"""

import subprocess
import sys
import os
import time

# Color codes
C = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
}

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    clear()
    banner = f"""
{C['cyan']}{C['bold']}
   ╔═══════════════════════════════════════════╗
   ║   📦 HCO-MITM PACKAGE INSTALLER 📦        ║
   ║   🚀 One-click Setup for Termux/Linux     ║
   ╚═══════════════════════════════════════════╝
{C['reset']}
{C['yellow']}🔧 This script will install all required packages...
{C['reset']}
"""
    print(banner)

def run_command(cmd, description):
    """Run a shell command with visual feedback"""
    print(f"{C['blue']}▶ {description}...{C['reset']}")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Animation while running
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    i = 0
    while process.poll() is None:
        sys.stdout.write(f"\r{C['yellow']}   {chars[i % len(chars)]} Processing...{C['reset']}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    
    if process.returncode == 0:
        sys.stdout.write(f"\r{C['green']}   ✓ {description} completed successfully.{C['reset']}\n")
        return True
    else:
        sys.stdout.write(f"\r{C['red']}   ✗ {description} failed.{C['reset']}\n")
        return False

def install_package(pkg_name, install_cmd):
    """Install a single package with progress"""
    print(f"{C['cyan']}📦 Installing {pkg_name}...{C['reset']}")
    # Simulate progress with loading bar
    steps = 10
    for i in range(steps+1):
        percent = i * 10
        bar = "█" * i + "░" * (steps - i)
        sys.stdout.write(f"\r   [{C['green']}{bar}{C['reset']}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.15)
    # Actual install
    result = subprocess.run(install_cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        sys.stdout.write(f"\r   [{C['green']}{'█'*10}{C['reset']}] 100% {C['green']}✓ Installed{C['reset']}\n")
        return True
    else:
        sys.stdout.write(f"\r   [{C['red']}{'█'*10}{C['reset']}] 100% {C['red']}✗ Failed{C['reset']}\n")
        print(f"{C['red']}Error: {result.stderr[:200]}{C['reset']}")
        return False

def main():
    print_banner()
    time.sleep(1)
    
    # Check if running as root (not required but helpful)
    is_root = (os.geteuid() == 0) if hasattr(os, 'geteuid') else False
    if is_root:
        print(f"{C['green']}✓ Running as root - installation will be system-wide.{C['reset']}")
    else:
        print(f"{C['yellow']}⚠ Running as normal user - some packages may require sudo (Termux works).{C['reset']}")
    
    # Detect Termux
    is_termux = os.path.exists("/data/data/com.termux") or "termux" in os.getenv("PREFIX", "")
    if is_termux:
        print(f"{C['green']}✓ Termux environment detected.{C['reset']}")
        update_cmd = "pkg update -y"
        upgrade_cmd = "pkg upgrade -y"
        install_base = "pkg install -y"
        python_cmd = "pkg install python python-pip -y"
        git_cmd = "pkg install git -y"
        ping_cmd = "pkg install iputils-ping -y"
        iproute_cmd = "pkg install iproute2 -y"
    else:
        print(f"{C['blue']}✓ Linux environment detected (Debian/Ubuntu/Kali).{C['reset']}")
        update_cmd = "sudo apt update -y"
        upgrade_cmd = "sudo apt upgrade -y"
        install_base = "sudo apt install -y"
        python_cmd = "sudo apt install python3 python3-pip -y"
        git_cmd = "sudo apt install git -y"
        ping_cmd = "sudo apt install iputils-ping -y"
        iproute_cmd = "sudo apt install iproute2 -y"
    
    # Step-by-step installation
    packages = [
        ("System Update", update_cmd, False),
        ("System Upgrade", upgrade_cmd, False),
        ("Python & PIP", python_cmd, True),
        ("Git", git_cmd, True),
        ("Ping (iputils-ping)", ping_cmd, True),
        ("IPRoute2", iproute_cmd, True),
    ]
    
    success_count = 0
    for idx, (desc, cmd, show_progress) in enumerate(packages, 1):
        print(f"\n{C['bold']}[{idx}/{len(packages)}]{C['reset']} {desc}")
        if show_progress:
            # For packages, show detailed progress bar
            if install_package(desc, cmd):
                success_count += 1
            else:
                print(f"{C['red']}⚠ Continuing... (manual install may be required){C['reset']}")
        else:
            if run_command(cmd, desc):
                success_count += 1
        time.sleep(0.5)
    
    # Optional: Install colorama (Python package)
    print(f"\n{C['bold']}📦 Installing Python package: colorama (optional){C['reset']}")
    colorama_install = "pip install colorama" if not is_termux else "pip install colorama"
    if install_package("colorama", colorama_install):
        success_count += 1
    
    # Final status
    print(f"\n{C['bold']}{'='*50}{C['reset']}")
    if success_count == len(packages) + 1:
        print(f"{C['green']}{C['bold']}🎉 ALL PACKAGES INSTALLED SUCCESSFULLY! 🎉{C['reset']}")
        print(f"{C['green']}✅ You can now run: python3 HCO-MITM-Attack.py{C['reset']}")
    else:
        print(f"{C['yellow']}⚠ Some packages failed to install.{C['reset']}")
        print(f"{C['yellow']}Please check your internet connection and try again.{C['reset']}")
    
    print(f"{C['cyan']}Thank you for using HCO-MITM Framework!{C['reset']}\n")

if __name__ == "__main__":
    main()