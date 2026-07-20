# Main program

from checks.system_info import get_system_info
from checks.check_privileges import check_privileges
import checks.check_firewalls as firewall_check

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

print("""
Firewall Audit
---------------
""")

firewall_info = firewall_check.check_firewall()
for key, value in firewall_info.items():
    print(f"{key}: {value}")