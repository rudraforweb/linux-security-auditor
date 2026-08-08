import subprocess

def check_ssh():
    result = subprocess.run(["cat", "/etc/ssh/sshd_config"], capture_output=True, text=True)
    if "No such file or directory" in result.stderr:
        
        installed = False
    elif "Permission denied" in result.stderr:
        
        installed = True
    else:
    
        installed = True

    result = subprocess.run(["systemctl", "is-active", "sshd"], capture_output=True, text=True)
    if installed == False:
        active = False
    elif result.stdout.strip() == "active":
        active = True
    else:
        active = False

    return {
        "installed": installed,
        "active": active
    }
