import subprocess
import distro

def check_updates_apt():
    result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)
    if result.returncode == 0:
        line_count = len(result.stdout.splitlines())
        return {
            "upgradable_packages": line_count - 1 
        }
    else:
        return {
            "upgradable_packages": 0
        }

def check_updates_dnf():
    result = subprocess.run(["dnf", "check-update"], capture_output=True, text=True)
    if result.returncode == 100:
        return {
            "upgradable_packages": True
        }
    else:
        return {
            "upgradable_packages": False
        }

def check_updates():
    if distro.id() in ["ubuntu", "debian", "linuxmint"]:
        return check_updates_apt()
    elif distro.id() in ["fedora", "rhel", "centos"]:
        return check_updates_dnf()
    else:
        return {
            "upgradable_packages": "Unsupported distribution"
        }