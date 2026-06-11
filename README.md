# SHR--MITM-ATTACK


```markdown
<!--
============================================================
SHR-MITM - Advanced MITM Framework (No Root / Termux Compatible)
Author: THE SILENT HACKER RAJ 🚭
YouTube: https://youtube.com/@CYBER_SHR_1K
============================================================
-->

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.0-brightgreen?style=for-the-badge" alt="Version 3.0">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-Educational%20Only-red?style=for-the-badge" alt="License">
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=00FFAA&center=true&vCenter=true&width=600&lines=SHR-MITM+Advanced+Framework;Man+in+the+Middle+Simulator;No+Root+Required;Made+by+THE+SILENT+HACKER+RAJ+%F0%9F%9A%AD" alt="Typing SVG">
</p>

<br>

## 🛡️ SHR-MITM – Advanced MITM Framework

**SHR-MITM** is a powerful, educational man-in-the-middle simulation tool designed for **Termux** (Android) and **Linux** (Kali, Ubuntu).  
It performs **real network scanning** (ARP + ping) and **simulates** MITM attacks by capturing fake HTTP/HTTPS traffic, demonstrating how credentials can be intercepted over a local network.

> ⚠️ **FOR EDUCATIONAL USE ONLY** – Use only on your own network or with explicit permission. The author is not responsible for misuse.

---

## ✨ Features

- 🔍 **Fast Network Scanning** – Multi-threaded ping sweep (50 threads)  
- 🎯 **MITM Attack Simulation** – Live packet capture with realistic data  
- 🖥️ **No Root Required** – Works perfectly in Termux (non-root)  
- 📋 **Saved Device List** – Attack from previously scanned devices  
- 🎨 **Colorful Banner & UI** – Multi‑color ASCII art, easy menus  
- 🔐 **Credential Capture** – Simulated capture of passwords (educational)  
- 🚪 **Gateway & IP Info** – Show your network details  
- 📜 **One-Click Setup** – `packages.py` automates all installations  

---

## 📸 Preview (Language Icons)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Bash">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white" alt="Android Termux">
</p>

---

## 📦 Installation (Full Automated)

Follow the steps below. All commands are **copy‑paste** friendly – just click the copy icon on GitHub.

### 1️⃣ Update System & Install Prerequisites

<details>
<summary><b>🔧 Click to expand – Termux / Linux commands</b></summary>

<br>

#### For Termux (Android):
```bash
pkg update && pkg upgrade -y
pkg install python python-pip git iputils-ping iproute2 -y
chmod +x packages.py
```

For Linux (Kali/Debian/Ubuntu):

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git iputils-ping iproute2 -y
chmod +x packages.py
```

</details>

2️⃣ Run the Automated Installer

```bash
python3 packages.py
```

This script will install all required packages with a beautiful progress bar.

3️⃣ Download SHR-MITM (if not already)

```bash
git clone https://github.com/YOUR_USERNAME/SHR-MITM.git
cd SHR-MITM
```

⚠️ Replace YOUR_USERNAME with your actual GitHub username.

4️⃣ Run the Main Tool

```bash
python3 HCO-MITM-Attack.py
```

---

🎮 How to Use

After launching, you will see the subscription unlock screen.
Press ENTER after subscribing to the YouTube Channel.

Then use the interactive menu:

Option Description
1 🔍 SCAN NETWORK (Fast + Show all devices)
2 🎯 LAUNCH MITM ATTACK (Select target by ID)
3 📋 LIST SAVED DEVICES (Attack from saved list)
4 🌐 NETWORK INFO (Your IP & Gateway)
5 📜 VIEW CAPTURED CREDENTIALS
6 🚪 EXIT

💡 Tip: After scanning, you can directly attack any device using Option 2 or Option 3.

---

📁 File Structure

```
SHR-MITM/
├── HCO-MITM-Attack.py   # Main MITM tool
├── packages.py          # One‑click dependency installer
└── README.md            # This file
```

---

🧰 Requirements

· Python 3.6+
· ping and ip commands (installed automatically)
· Internet connection (for installation & YouTube unlock)

No third‑party Python packages required – uses only standard libraries.

---

🖼️ Screenshots (Conceptual)

<p align="center">
  <img src="https://via.placeholder.com/600x300?text=Banner+Preview" width="600">
</p>

---

👑 Credits

<p align="center">
  <b>Author:</b> THE SILENT HACKER RAJ 🚭<br>
  <b>YouTube:</b> <a href="https://youtube.com/@CYBER_SHR_1K">@CYBER_SHR_1K</a><br>
  <b>GitHub:</b> <a href="https://github.com/THE-SILENT-HACKER-RAJ">THE-SILENT-HACKER-RAJ</a><br>
  <i>“Stay silent, stay secure.”</i>
</p>

---

📜 License

This project is for educational purposes only.
You are not allowed to use it for illegal activities.
By using this software, you agree to the terms that the author holds no liability.

---

🌟 Support

If you like this tool, please star ⭐ the repository and subscribe to the YouTube channel.
For bugs or suggestions, open an Issue on GitHub.

<p align="center">
  <img src="https://img.shields.io/github/stars/THE-SILENT-HACKER-RAJ/SHR-MITM?style=social" alt="GitHub stars">
  <img src="https://img.shields.io/youtube/channel/subscribers/UC...?style=social" alt="YouTube subscribers">
</p>
