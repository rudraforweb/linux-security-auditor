# Main program

from checks.system_info import get_system_info
from checks.check_privileges import check_privileges

print("""
Linux Security Auditor
======================
      """)

system_info = get_system_info()
privilege_info = check_privileges()

report = {
    "system": system_info,
    "privileges": check_privileges
}

print("""
System Information
------------------
      """)

for key, value in system_info.items():
    print(f"{key}: {value}")

print("""
Privilege Audit
---------------
""")


for key, value in privilege_info.items():
    print(f"{key}: {value}")