import shutil
import subprocess

def check_ufw():
    if shutil.which('ufw') is not None:
        installed = True
    else:
        return {
            "ufw_installed": False,
            "active": False
        }


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


def check_firewalld():
    if shutil.which('firewall-cmd') is not None:
        installed = True
    else:
        installed = False
        return {
            "firewalld_installed": installed,
            "active": False
        }

    result = subprocess.run(["firewall-cmd", "--state"], capture_output=True, text=True)
    if "not running" in result.stdout or "not running" in result.stderr:
        active = False
    elif "running" in result.stdout:
        active = True
    else:
        active = "Requires root privileges"
    
    return {
        "firewalld_installed": installed,
        "active": active
    }

def check_firewall():
    ufw = check_ufw()
    firewalld = check_firewalld()

    if ufw["active"]:
        return {
            "firewall": "ufw",
            "installed": ufw["ufw_installed"],
            "active": ufw["active"]
        }
    elif firewalld["active"]:
        return {
            "firewall": "firewalld",
            "installed": firewalld["firewalld_installed"],
            "active": firewalld["active"]
        }
    else:
        return {
            "firewall": None,
            "installed": False,
            "active": False
        }