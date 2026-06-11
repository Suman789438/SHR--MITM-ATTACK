#!/usr/bin/env python3
"""
SHR MITM - Advanced MITM Framework (No Root / Termux Compatible)
Educational Purpose Only - Simulated Attack Mode with Real Network Scan
"""

import os
import sys
import time
import socket
import threading
import subprocess
import random
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Enhanced color codes
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
    'underline': '\033[4m',
    'orange': '\033[38;5;208m',
    'pink': '\033[38;5;205m',
    'lblue': '\033[38;5;81m',
}

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def type_effect(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading(text="LOADING", duration=2):
    chars = "█▓▒░"
    end = time.time() + duration
    i = 0
    while time.time() < end:
        progress = int((end - time.time()) / duration * 20)
        bar = chars[i % len(chars)] * 20
        sys.stdout.write(f"\r{C['cyan']}[{bar}] {text} {progress}%{C['reset']}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f"\r{C['green']}[✓] {text} COMPLETE           {C['reset']}")

def banner():
    clear()
    banner_text = f"""
{C['red']}{C['bold']}   ███████╗██╗  ██╗██████╗     {C['yellow']}███╗   ███╗██╗████████╗███╗   ███╗{C['reset']}
{C['green']}{C['bold']}   ██╔════╝██║  ██║██╔══██╗    {C['lblue']}████╗ ████║██║╚══██╔══╝████╗ ████║{C['reset']}
{C['blue']}{C['bold']}   ███████╗███████║██████╔╝    {C['magenta']}██╔████╔██║██║   ██║   ██╔████╔██║{C['reset']}
{C['cyan']}{C['bold']}   ╚════██║██╔══██║██╔══██╗    {C['orange']}██║╚██╔╝██║██║   ██║   ██║╚██╔╝██║{C['reset']}
{C['pink']}{C['bold']}   ███████║██║  ██║██║  ██║    {C['red']}██║ ╚═╝ ██║██║   ██║   ██║ ╚═╝ ██║{C['reset']}
{C['yellow']}{C['bold']}   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    {C['green']}╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝     ╚═╝{C['reset']}

{C['cyan']}{C['bold']}          ⚡ ADVANCED MITM FRAMEWORK (NON ROOT) ⚡{C['reset']}
{C['yellow']}        👤 Author: the_silent_hacker_raj | 📺 YouTube: @CYBER_SHR_1K{C['reset']}
{C['red']}       🔐 FOR EDUCATIONAL USE ONLY ON YOUR NETWORK{C['reset']}
    """
    print(banner_text)
    time.sleep(1)

class SHR_MITM:
    def __init__(self):
        self.devices = []
        self.captured = []
        self.running = False

    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

    def get_hostname(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return "Unknown"

    def get_mac_vendor(self, ip):
        """Get MAC address using ARP table or /proc/net/arp (Termux friendly)"""
        mac = "N/A"
        vendor = "Unknown"
        try:
            result = subprocess.run(f"ip neigh show {ip}", shell=True, capture_output=True, text=True, timeout=2)
            if result.stdout:
                parts = result.stdout.split()
                for p in parts:
                    if re.match(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", p):
                        mac = p.upper()
                        break
        except:
            pass
        
        if mac == "N/A":
            try:
                with open("/proc/net/arp", "r") as f:
                    for line in f:
                        if ip in line:
                            parts = line.split()
                            if len(parts) >= 4:
                                mac = parts[3].upper()
                                break
            except:
                pass
        
        if mac != "N/A" and len(mac) >= 8:
            oui = mac[:8]
            oui_db = {
                "B8:27:EB": "Raspberry Pi",
                "DC:A6:32": "Apple",
                "EC:08:6B": "Apple",
                "00:11:22": "Cisco",
                "00:1A:2B": "Samsung",
                "70:3A:CB": "OnePlus",
                "18:9E:FC": "Xiaomi",
                "C4:85:08": "TP-Link",
            }
            vendor = oui_db.get(oui, "Generic Device")
        return mac, vendor

    def ping_host(self, ip):
        """Ping a single host, return ip if reachable"""
        try:
            # Use ping with short timeout (0.5 sec) for speed
            res = subprocess.run(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1", shell=True, timeout=1)
            if res.returncode == 0:
                return ip
        except:
            pass
        return None

    def scan_network(self):
        """Fast threaded network scan without root"""
        print(f"\n{C['cyan']}{C['bold']}[🔍] SCANNING NETWORK (Fast Mode)...{C['reset']}")
        loading("THREADED PING SCAN", 1)
        
        local_ip = self.get_local_ip()
        prefix = '.'.join(local_ip.split('.')[:-1]) + '.'
        print(f"{C['yellow']}[*] Network range: {prefix}1-254{C['reset']}")
        
        active = [local_ip]  # always include own IP
        ips = [f"{prefix}{i}" for i in range(1, 255) if f"{prefix}{i}" != local_ip]
        
        # Use thread pool for fast ping sweep
        with ThreadPoolExecutor(max_workers=50) as executor:
            future_to_ip = {executor.submit(self.ping_host, ip): ip for ip in ips}
            completed = 0
            for future in as_completed(future_to_ip):
                completed += 1
                ip = future_to_ip[future]
                result = future.result()
                if result:
                    active.append(result)
                if completed % 30 == 0:
                    sys.stdout.write(f"\r{C['blue']}[+] Scanned {completed}/{len(ips)} hosts...{C['reset']}")
                    sys.stdout.flush()
        
        print(f"\r{C['green']}[✓] Found {len(active)} active devices{C['reset']}")
        
        devices = []
        for idx, ip in enumerate(active):
            host = self.get_hostname(ip)
            mac, vendor = self.get_mac_vendor(ip)
            devices.append({
                'id': idx+1,
                'ip': ip,
                'hostname': host,
                'mac': mac,
                'vendor': vendor
            })
        
        self.devices = devices
        self.show_devices()
        return devices

    def show_devices(self):
        print(f"\n{C['magenta']}{'ID':<4} {'IP Address':<16} {'Hostname':<28} {'MAC Address':<18} {'Vendor'}{C['reset']}")
        print(f"{C['yellow']}{'-'*90}{C['reset']}")
        for d in self.devices:
            print(f"{C['green']}{d['id']:<4} {C['cyan']}{d['ip']:<16} {C['white']}{d['hostname'][:27]:<28} {C['yellow']}{d['mac']:<18} {C['magenta']}{d['vendor']}{C['reset']}")

    def simulate_attack(self, target_ip, target_name):
        """Realistic MITM simulation with live captured data"""
        print(f"\n{C['red']}{C['bold']}[⚡] INITIATING MITM ATTACK ON {target_ip} ({target_name}){C['reset']}")
        loading("ARP POISONING", 1)
        loading("SPOOFING GATEWAY", 1)
        loading("SNIFFING TRAFFIC", 1)
        
        print(f"{C['green']}[✓] Man-in-the-middle position established{C['reset']}")
        print(f"{C['yellow']}[*] Monitoring HTTP/HTTPS traffic... Press Ctrl+C to stop{C['reset']}\n")
        
        packets = [
            ("HTTP", target_ip, "google.com", "GET /search?q=bank+login"),
            ("HTTP", target_ip, "facebook.com", "POST /login.php", "email=hacker@test.com&pass=secret123"),
            ("DNS", target_ip, "8.8.8.8", "Query: paypal.com"),
            ("HTTP", target_ip, "paypal.com", "POST /cgi-bin/webscr", "login=user@paypal.com&password=myp@ssword"),
            ("HTTPS", target_ip, "gmail.com", "GET /mail", "[ENCRYPTED]"),
            ("HTTP", target_ip, "instagram.com", "POST /accounts/login", "username=target_user&password=instaPass"),
            ("DNS", target_ip, "1.1.1.1", "Query: icicibank.co.in"),
            ("HTTP", target_ip, "netflix.com", "GET /browse", "sessionid=abc123"),
        ]
        
        self.running = True
        packet_count = 0
        for pkt in packets:
            if not self.running:
                break
            packet_count += 1
            ts = datetime.now().strftime("%H:%M:%S")
            if len(pkt) == 5 and pkt[4]:
                protocol, src, dst, action, data = pkt
                color = C['red'] if "password" in data.lower() else C['yellow']
                print(f"{color}[{ts}] {protocol} {src} -> {dst} | {action}{C['reset']}")
                print(f"{color}    📦 DATA: {data[:100]}{C['reset']}")
                if "password" in data.lower() or "pass=" in data:
                    print(f"{C['red']}{C['bold']}    🔐 CREDENTIAL CAPTURED: {data}{C['reset']}")
                    self.captured.append((ts, data))
            else:
                protocol, src, dst, action = pkt[:4]
                print(f"{C['cyan']}[{ts}] {protocol} {src} -> {dst} | {action}{C['reset']}")
            time.sleep(random.uniform(1.5, 3))
            sys.stdout.write(f"\r{C['magenta']}[📊] Captured packets: {packet_count}{C['reset']}")
            sys.stdout.flush()
        
        print(f"\n\n{C['green']}[✓] Attack simulation completed. Total packets: {packet_count}{C['reset']}")
        if self.captured:
            print(f"{C['red']}[!] {len(self.captured)} sensitive credentials logged!{C['reset']}")

    def show_captured(self):
        if not self.captured:
            print(f"{C['yellow']}[*] No captured data yet. Run an attack first.{C['reset']}")
        else:
            print(f"\n{C['red']}{C['bold']}[📜] CAPTURED DATA LOG:{C['reset']}")
            for ts, data in self.captured:
                print(f"{C['red']}[{ts}] {data}{C['reset']}")

    def network_info(self):
        ip = self.get_local_ip()
        print(f"\n{C['green']}[🌐] Your Local IP: {ip}{C['reset']}")
        try:
            gw = subprocess.run("ip route | grep default | awk '{print $3}'", shell=True, capture_output=True, text=True)
            if gw.stdout:
                print(f"{C['blue']}[🚪] Gateway: {gw.stdout.strip()}{C['reset']}")
        except:
            pass
        input(f"\n{C['cyan']}Press Enter...{C['reset']}")

    def show_saved_devices(self):
        """Display saved devices list and allow attack directly from list"""
        if not self.devices:
            print(f"\n{C['red']}[!] No saved devices found. Please scan network first (Option 1).{C['reset']}")
            input(f"\n{C['cyan']}Press Enter...{C['reset']}")
            return
        self.show_devices()
        try:
            tid = int(input(f"\n{C['white']}Enter target ID to attack: {C['reset']}"))
            target = next((d for d in self.devices if d['id'] == tid), None)
            if not target:
                print(f"{C['red']}Invalid ID{C['reset']}")
                input(f"\n{C['cyan']}Press Enter...{C['reset']}")
                return
            confirm = input(f"{C['red']}Start MITM attack on {target['ip']} ({target['hostname']})? (y/N): {C['reset']}")
            if confirm.lower() == 'y':
                self.simulate_attack(target['ip'], target['hostname'])
        except ValueError:
            print(f"{C['red']}Enter a valid number{C['reset']}")
        input(f"\n{C['cyan']}Press Enter...{C['reset']}")

    def unlock_with_subscription(self):
        """YouTube subscription unlock screen"""
        clear()
        banner()
        print(f"\n{C['red']}{C['bold']}🔒 TOOL LOCKED - SUBSCRIBE TO UNLOCK 🔒{C['reset']}")
        print(f"{C['yellow']}📺 YouTube Channel: {C['cyan']}https://youtube.com/@CYBER_SHR_1K{C['reset']}")
        print(f"{C['green']}💡 Please subscribe and then press ENTER to continue...{C['reset']}")
        try:
            # Try to open URL automatically (optional)
            if sys.platform == "linux":
                subprocess.Popen(["termux-open-url", "https://youtube.com/@CYBER_SHR_1K"])
            else:
                subprocess.Popen(["xdg-open", "https://youtube.com/@CYBER_SHR_1K"])
        except:
            pass
        input(f"\n{C['magenta']}👉 Press ENTER after subscribing: {C['reset']}")
        print(f"{C['green']}[✓] Tool unlocked! Welcome back.{C['reset']}")
        time.sleep(1)

    def menu(self):
        self.unlock_with_subscription()  # Enforce subscription check at start
        while True:
            banner()
            print(f"""
{C['cyan']}{C['bold']}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C['reset']}
{C['yellow']}  [1] 🔍 SCAN NETWORK (Fast + Show all devices)
{C['green']}  [2] 🎯 LAUNCH MITM ATTACK (Select target by ID)
{C['lblue']}  [3] 📋 LIST SAVED DEVICES (Attack from list)
{C['blue']}  [4] 🌐 NETWORK INFO (Your IP & Gateway)
{C['magenta']}  [5] 📜 VIEW CAPTURED CREDENTIALS
{C['red']}  [6] 🚪 EXIT
{C['cyan']}{C['bold']}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C['reset']}
            """)
            choice = input(f"{C['white']}[SHR-MITM] >>> {C['reset']}").strip()
            
            if choice == '1':
                self.scan_network()
                input(f"\n{C['cyan']}Press Enter...{C['reset']}")
            elif choice == '2':
                if not self.devices:
                    print(f"{C['red']}[!] Please scan network first (option 1){C['reset']}")
                    time.sleep(1.5)
                    continue
                self.show_devices()
                try:
                    tid = int(input(f"\n{C['white']}Enter target ID: {C['reset']}"))
                    target = next((d for d in self.devices if d['id'] == tid), None)
                    if not target:
                        print(f"{C['red']}Invalid ID{C['reset']}")
                        continue
                    confirm = input(f"{C['red']}Start MITM attack on {target['ip']} ({target['hostname']})? (y/N): {C['reset']}")
                    if confirm.lower() == 'y':
                        self.simulate_attack(target['ip'], target['hostname'])
                except ValueError:
                    print(f"{C['red']}Enter a number{C['reset']}")
                input(f"\n{C['cyan']}Press Enter...{C['reset']}")
            elif choice == '3':
                self.show_saved_devices()
            elif choice == '4':
                self.network_info()
            elif choice == '5':
                self.show_captured()
                input(f"\n{C['cyan']}Press Enter...{C['reset']}")
            elif choice == '6':
                print(f"{C['green']}Exiting SHR MITM. Stay ethical!{C['reset']}")
                sys.exit(0)
            else:
                print(f"{C['red']}Invalid option{C['reset']}")
                time.sleep(1)

def main():
    tool = SHR_MITM()
    tool.menu()

if __name__ == "__main__":
    main()