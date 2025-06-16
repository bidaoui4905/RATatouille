# clean.py
import subprocess

def delete_screenshots():
    subprocess.run([
        "powershell",
        "Remove-Item $env:USERPROFILE\\Documents\\ScreenShot\\*.*"
    ], shell=False)
    print("[+] Screenshots deleted.")
