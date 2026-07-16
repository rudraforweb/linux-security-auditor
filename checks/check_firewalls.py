import shutil
import subprocess
def check_ufw():
    if shutil.which('ufw') is not None:
        installed = True
    else:
        installed = False

    result = subprocess.run(["ufw", "status"], capture_output=True, text=True)
    if "ERROR" in result.stdout or "ERROR" in result.stderr:
        active = "Requires root privileges"
    elif "inactive" not in result.stdout:
        active = True
    else:
        active = False
    
    return {
        "ufw_installed": installed,
        "active": active
    }

