import os
import getpass
import grp

def check_admin_access():
    groups = []

    for gid in os.getgroups():
        groups.append(grp.getgrgid(gid).gr_name)

    return "sudo" in groups or "wheel" in groups

def check_privileges():
    username = getpass.getuser()
    root = os.geteuid() == 0
    
    admin_access = check_admin_access()

    return {
        "user": username,
        "running_as_root": root,
        "admin_access": admin_access
    }

print(check_privileges())